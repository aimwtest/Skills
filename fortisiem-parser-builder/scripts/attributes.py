#!/usr/bin/env python3
"""Search the actual catalog or audit explicit parser output targets. Not an FSM engine."""
import argparse
import collections
import csv
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r'<([A-Za-z_][\w.-]*)?:([A-Za-z_][\w.-]*)>')

def catalog(path):
    rows = list(csv.DictReader(Path(path).open(encoding='utf-8-sig', newline='')))
    required = {'name', 'value_type', 'display_name'}
    if not rows or not required <= rows[0].keys():
        raise ValueError('Catalog needs name, value_type and display_name columns')
    counts = collections.Counter(r['name'] for r in rows)
    duplicate = [n for n, c in counts.items() if c > 1]
    if duplicate:
        raise ValueError('Ambiguous duplicate names: ' + ', '.join(duplicate))
    html = (ROOT / 'references/FSM-ParserBuilder_v0.9.1.html').read_text()
    types = dict(re.findall(r"\{name:'([^']+)', display:'(?:\\.|[^'])*', type:'([^']+)'\}", html))
    votes = collections.defaultdict(collections.Counter)
    for row in rows:
        if row['name'] in types:
            votes[row['value_type']][types[row['name']]] += 1
    resolved = {k: next(iter(v)) for k, v in votes.items() if len(v) == 1}
    for row in rows:
        row['resolved_type'] = resolved.get(row['value_type'], 'UNRESOLVED')
        row['type_evidence'] = 'CSV code / ParserBuilder same-name consensus; not an official enum'
        row['scope'] = {'t':'system', 'true':'system', 'f':'user', 'false':'user'}.get(row.get('sys_defined','').lower(), 'unknown')
        if Path(path).resolve() == (ROOT / 'references/fortisiem_event_attributes.csv').resolve():
            if not row.get('attr_id', '').isdigit() or int(row['attr_id']) >= 10000:
                raise ValueError('Bundled system catalog violates user rule attr_id < 10000')
            row['scope'] = 'system (user-confirmed attr_id < 10000 rule)'
    return {r['name']: r for r in rows}, {k: dict(v) for k, v in votes.items()}

def audit(xml, rows):
    # FortiSIEM editor syntax is an XML fragment. The wrapper exists only in memory.
    if re.search(r'<!DOCTYPE|<!ENTITY', xml, re.I):
        raise ValueError('DTD/entity declarations are not supported')
    xml = re.sub(r'^\s*<\?xml[^?]*\?>', '', xml)
    root = ET.fromstring('<auditRoot>' + xml + '</auditRoot>')
    for required in ['eventFormatRecognizer', 'parsingInstructions']:
        if len(list(root.iter(required))) != 1:
            raise ValueError('Expected exactly one ' + required)
    # XML attributes plus FortiSIEM capture targets INSIDE CDATA.
    targets = {n.attrib['attr'] for n in root.iter() if 'attr' in n.attrib}
    patterns = set()
    refs = set()
    for n in root.iter():
        if n.tag == 'pattern':
            patterns.add(n.attrib.get('name', ''))
        if n.tag in ('regex', 'eventFormatRecognizer', 'pattern'):
            for target, pat in TOKEN.findall(n.text or ''):
                if target: targets.add(target)
                refs.add(pat)
    html = (ROOT / 'references/FSM-ParserBuilder_v0.9.1.html').read_text()
    builtins = set(re.findall(r'\["(gPat\w+)",', html))
    temp = sorted(n for n in targets if n.startswith('_'))
    persisted = sorted(targets - set(temp))
    missing = sorted(n for n in persisted if n not in rows)
    existing = [rows[n] for n in persisted if n in rows]
    return {
        'validation_level':'XML structure + explicit output-target inventory only',
        'xml_structure':'passed', 'catalog_rows':len(rows),
        'existing_attributes':existing,
        'additional_attribute_names':missing,
        'temporary_variables':temp,
        'patterns_not_in_local_catalog':sorted(refs - patterns - builtins),
        'unresolved_types':[r['name'] for r in existing if r['resolved_type']=='UNRESOLVED'],
        'manual_checks':['branch definite assignment', 'implicit/dynamic attribute setters',
                         'field meaning and units', 'runtime optional-field behavior',
                         'official syntax and function signatures', 'FortiSIEM Validate/Test'],
    }

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--catalog', default=str(ROOT / 'references/fortisiem_event_attributes.csv'))
    g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--search', help='Case-insensitive substring over name, display name, description')
    g.add_argument('--xml', type=Path)
    g.add_argument('--summary', action='store_true')
    a=p.parse_args()
    try:
        rows,votes=catalog(a.catalog)
        if a.search is not None:
            q=a.search.casefold()
            result=[r for r in rows.values() if q in ' '.join(r.get(k,'') for k in ('name','display_name','description')).casefold()]
        elif a.xml:
            result=audit(a.xml.read_text(encoding='utf-8-sig'), rows)
        else:
            result={'rows':len(rows),'scope_counts':dict(collections.Counter(r['scope'] for r in rows.values())), 'type_code_evidence':votes}
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, ET.ParseError, OSError) as e:
        print(json.dumps({'error':str(e)}, ensure_ascii=False))
        return 2
    return 0

if __name__ == '__main__':
    sys.exit(main())
