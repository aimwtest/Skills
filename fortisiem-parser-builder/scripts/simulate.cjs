#!/usr/bin/env node
// Run the user's original ParserBuilder in local Chromium. No external requests.
const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const {createRequire} = require('node:module');
let playwright;
try { playwright = require('playwright'); }
catch {
  const base = process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES;
  if (!base) throw Error('Playwright unavailable; report simulation as not run.');
  playwright = createRequire(path.join(base, '_resolver.cjs'))('playwright');
}
async function main() {
  const [xmlPath, logsPath] = process.argv.slice(2);
  if (!xmlPath || !logsPath) throw Error('Usage: node simulate.cjs parser.xml samples.json');
  const xml=fs.readFileSync(xmlPath,'utf8');
  const logs=JSON.parse(fs.readFileSync(logsPath,'utf8'));
  if (!Array.isArray(logs) || logs.some(x => typeof x !== 'string')) throw Error('samples.json must be an array of raw log strings');
  const executablePath=process.env.FSM_PARSER_CHROMIUM;
  const browser=await playwright.chromium.launch({headless:true, ...(executablePath ? {executablePath} : {})});
  try {
    const page=await browser.newPage();
    await page.route('**/*', route => route.request().url().startsWith('file:') ? route.continue() : route.abort());
    await page.goto(pathToFileURL(path.resolve(__dirname,'../references/FSM-ParserBuilder_v0.9.1.html')).href);
    const result=await page.evaluate(({xml,logs}) => {
      resetIterateStepsCache(); resetPatternMapCache();
      const block=recognizerBlock(xml);
      if (!block) throw Error('Missing recognizer');
      const re=compileFortiPattern(block.body,patternMap(xml,block.start),[]);
      return logs.map((log,i) => {
        // Original simulateLogState runs instructions even when recognizer fails.
        // Gate explicitly so rejected logs cannot look successfully parsed.
        if (!re.test(log)) return {sample:i+1,recognizer:false,attributes:{},variables:{}};
        const state=simulateLogState(xml,xml.length,log);
        const simplify = map => Object.fromEntries([...map].map(([k,v]) => [k,{value:v.value,computed:!!v.computed}]));
        return {sample:i+1,recognizer:true,attributes:simplify(state.attributes),variables:simplify(state.variables)};
      });
    },{xml,logs});
    console.log(JSON.stringify({engine:'ParserBuilder v0.9.1 / JavaScript simulation only',
      limitations:['computed functions are unresolved, not validated values','optional extraction and branch failures may differ from FortiSIEM','attribute types require CSV audit; HTML catalog may be stale'],results:result},null,2));
  } finally {await browser.close();}
}
main().catch(e=>{console.error(e.message);process.exitCode=2;});
