# Catalog and testing

Set `SKILL_DIR` to this skill's actual current directory. Helpers resolve bundled resources relative to themselves.

```bash
python3 "$SKILL_DIR/scripts/attributes.py" --summary
python3 "$SKILL_DIR/scripts/attributes.py" --search 'request'
python3 "$SKILL_DIR/scripts/attributes.py" --xml /absolute/ProductParser.xml
python3 "$SKILL_DIR/scripts/attributes.py" --catalog /absolute/new.csv --xml /absolute/ProductParser.xml
node "$SKILL_DIR/scripts/simulate.cjs" /absolute/ProductParser.xml /absolute/samples.json
```

`samples.json` is an array of unchanged raw-log strings (multiline events permitted). Simulation requires Node, Playwright and Chromium. If unavailable, report not run; do available static checks, never call a different simulator ParserBuilder.

## Snapshot facts and types

The original CSV contained 3,307 unique names. Per the user's explicit environment rule, remove all 16 rows with `attr_id >= 10000`; the bundled system-only catalog contains 3,291 rows with `attr_id < 10000`. All retained `sys_defined` values are blank. System classification comes from the user-confirmed ID rule, not from treating blank as true or false. The helper labels this evidence explicitly. A name outside this baseline is a creation dependency unless the user separately confirms it already exists; do not claim it is universally non-built-in in every FortiSIEM release. The prior export query excluded deprecated rows, but this snapshot lacks a deprecated column; do not claim a separate deprecation audit.

The HTML contains 3,268 attribute entries. All overlapping type-code groups agree in this snapshot:

| value_type | Label |
|---|---|
| 1 | STRING |
| 3 | UCHAR |
| 4 | INT16 |
| 5 | UINT16 |
| 6 | INT32 |
| 7 | UINT32 |
| 9 | UINT64 |
| 10 | IP |
| 11 | DATE |
| 12 | BINARY |
| 14 | DOUBLE |
| 15 | BINHEX |

These are cross-source consensus, not a published universal database enum. The helper recomputes mappings and marks conflicts/unmapped codes UNRESOLVED. Preserve numeric codes in the inventory; use confirmed readable types for new fields. Elasticsearch type alone cannot distinguish UINT16 and UINT32. Display format and units also matter.

`mandatory` does not mean every parser must set every marked row. Search meaning, not near-spelling. `httpRequestsPerSec` is a rate; `observed_rate=2000` and a separate 60-second window do not establish whether 2000 is per-second or a window count. Clarify/consult vendor docs before dividing or mapping to a per-second field.

## Validation scope

`attributes.py` validates a fragment with an in-memory wrapper, inventories `attr=` and CDATA capture targets (including local patterns), separates underscore locals and calculates absent names. Unknown patterns mean absent from the local catalog, not necessarily absent from FortiSIEM. Manually review implicit/dynamic setters, branch definite assignment, official signatures and field semantics.

`simulate.cjs` runs unchanged HTML locally, blocks network requests, checks recognizer separately, then invokes the original simulator. This gate matters: HTML `simulateLogState` continues through instructions even when recognition fails. `computed: true` marks unresolved functions such as toDateTime. Do not use the HTML's embedded attribute table over the CSV.

Compare expected results independently, including IP validity, integer ranges, decimals, units, direction, timestamp policy and classification. JavaScript regex and approximate optional-field/branch/XPath/array behavior are not the FortiSIEM runtime. Each delivery separates static checks, actual simulation/unresolved operations, and actual FortiSIEM Validate/Test (usually not run).

Use meaningful sample variants and a negative log, not an exhaustive synthetic suite. Keep customer fixtures in task deliverables, not permanently in the skill unless requested.
