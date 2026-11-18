#!/usr/bin/env python3
"""Offline structural check of a FortiSOAR solution-pack ZIP. Reads the ZIP only: no network, no credentials.

Usage: check_pack.py PACK.zip [--allow-active]
Exit 0 when there are no errors. Passing means "well-formed", never "imports cleanly": import is only proven on an appliance.
"""
import hashlib, json, re, sys, zipfile
from pathlib import PurePosixPath

SECRET = re.compile(r'(password|passwd|secret|api[_-]?key|bearer\s+[A-Za-z0-9._-]{12,}|eyJ[A-Za-z0-9_-]{20,})', re.I)
REQUIRED_INFO = ('name', 'version', 'type', 'label', 'publisher', 'contents')


def main(argv):
    if not argv or argv[0].startswith('-'):
        print(__doc__); return 2
    allow_active = '--allow-active' in argv
    errors, notes = [], []
    z = zipfile.ZipFile(argv[0])
    if z.testzip() is not None:
        errors.append('ZIP integrity failure')
    names = z.namelist()
    for n in names:
        p = PurePosixPath(n)
        if p.is_absolute() or '..' in p.parts or '\\' in n:
            errors.append('unsafe member path: ' + n)
    roots = {n.split('/')[0] for n in names}
    root = ''
    if len(roots) == 1 and all('/' in n for n in names):
        root = roots.pop() + '/'
        notes.append('upload layout: one enclosing directory ' + root)
    elif 'info.json' not in names:
        errors.append('no info.json at the top level or inside a single enclosing directory')
    get = lambda n: z.read(root + n)
    if root + 'info.json' not in names:
        errors.append('info.json missing'); return report(errors, notes)
    info = json.loads(get('info.json'))
    for k in REQUIRED_INFO:
        if k not in info:
            errors.append('info.json missing key: ' + k)
    if info.get('type') != 'solutionpack':
        errors.append('info.json type must be "solutionpack"')
    if root and root != '%s-%s/' % (info.get('name'), info.get('version')):
        errors.append('enclosing directory %r is not <name>-<version>' % root)
    jsons = {}
    for n in names:
        if n.endswith('.json'):
            try:
                jsons[n[len(root):]] = json.loads(z.read(n))
            except ValueError as e:
                errors.append('invalid JSON: %s (%s)' % (n, e))
        if SECRET.search(z.read(n).decode('utf-8', 'replace')):
            notes.append('possible secret-like text in %s: review it by hand' % n)
    sums = root + 'docs/checksums.sha256'
    if sums in names:
        listed = {}
        for line in z.read(sums).decode().splitlines():
            h, _, name = line.partition('  ')
            listed[name] = h
        for n in names:
            rel = n[len(root):]
            if rel == 'docs/checksums.sha256':
                continue
            if rel not in listed:
                errors.append('not in checksums: ' + rel)
            elif listed[rel] != hashlib.sha256(z.read(n)).hexdigest():
                errors.append('checksum mismatch: ' + rel)
        for rel in listed:
            if root + rel not in names:
                errors.append('checksum lists a missing member: ' + rel)
    else:
        notes.append('no docs/checksums.sha256 (optional, but recommended)')
    workflows = {}
    for rel, data in jsons.items():
        if rel.startswith('playbooks/') and not rel.endswith('collection.metadata.json') and isinstance(data, dict) and 'steps' in data:
            workflows[data['uuid']] = data
            steps = {s['uuid'] for s in data['steps']}
            if len(steps) != len(data['steps']):
                errors.append(rel + ': duplicate step uuid')
            if data.get('triggerStep', '').rsplit('/', 1)[-1] not in steps:
                errors.append(rel + ': triggerStep is not one of its steps')
            for r in data['routes']:
                for end in ('sourceStep', 'targetStep'):
                    if r[end].rsplit('/', 1)[-1] not in steps:
                        errors.append('%s: route %r %s missing' % (rel, r.get('name'), end))
            if data.get('isActive') and not allow_active:
                errors.append(rel + ': workflow is active (use --allow-active if intended)')
    for rel, data in jsons.items():
        if rel.startswith('records/') and isinstance(data, list):
            for rec in data:
                for st in (rec.get('steps') or {}).get('Steps', []):
                    ref = st.get('playbookIRI', '').rsplit('/', 1)[-1]
                    if ref and ref not in workflows:
                        errors.append('%s: record references a workflow not in the pack: %s' % (rel, ref))
    contents = info.get('contents', {})
    for rs in contents.get('recordSets', []):
        files = [r for r in jsons if r.startswith('records/%s/' % rs.get('apiName'))]
        count = sum(len(jsons[f]) for f in files)
        if count != rs.get('count'):
            errors.append('recordSet %s declares %s records, found %s' % (rs.get('apiName'), rs.get('count'), count))
    for pb in contents.get('playbooks', []):
        if not any(n.startswith(root + 'playbooks/' + pb['name'] + '/') for n in names):
            errors.append('contents lists playbook collection %r with no folder' % pb['name'])
    return report(errors, notes)


def report(errors, notes):
    for n in notes:
        print('note:', n)
    for e in errors:
        print('ERROR:', e)
    print('%d error(s). Offline check only; import and runtime are NOT verified.' % len(errors))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
