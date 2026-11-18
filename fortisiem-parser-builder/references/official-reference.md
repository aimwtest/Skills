# Official syntax — FortiSIEM 7.6.0

Verified 2026-09-09 by reading the actual official HTML pages below. Search reads returned 403; ordinary HTTPS retrieval successfully returned the document bodies. These are focused summaries, not a complete manual. Fetch linked sections for unfamiliar functions.

## Structure and identity

[Parser Specification](https://docs.fortinet.com/document/fortisiem/7.6.0/user-guide/564765/parser-specification): the definition comprises sibling `patternDefinitions`, `eventFormatRecognizer` and `parsingInstructions`. A generic XML parser needs a temporary wrapper. Do not ship an invented `<parser>` root just to make ElementTree accept it.

[Event Format Recognizer](https://docs.fortinet.com/document/fortisiem/7.6.0/user-guide/836070/event-format-recognizer-specification): regex in CDATA selects eligible logs and can reference local/built-in patterns. Use distinguishing product syntax tolerant of changing values, not a catch-all.

[General Parsing Patterns](https://docs.fortinet.com/document/fortisiem/7.6.0/user-guide/204115/general-parsing-patterns) is the next official reference for local definitions (link discovered, full page not frozen here). Check built-in patterns through the official navigation. HTML `GENERAL_PATTERNS` is a useful candidate list, not proof of all official definitions.

## Variables and branching

[Parsing Instructions — user-specified primary reference](https://docs.fortinet.com/document/fortisiem/7.6.0/user-guide/229719/parsing-instructions): attributes are registered in Admin → Device Support → Event Attributes with System/User scope. Underscores for locals are a readability convention, not an enforced requirement. This skill uses them consistently for auditable persistence intent.

[Setting Event Attributes](https://docs.fortinet.com/document/fortisiem/7.6.0/user-guide/517253/setting-event-attributes): a setter contains a literal, `$variable`, or supported function call. `attr` is the target without `$`; source expressions use `$`. Do not quote literal text as if writing Python.

[When Construct](https://docs.fortinet.com/document/fortisiem/7.6.0/user-guide/517904/when-construct): supports equality, inequality, IN, matches/not_matches, exist/not_exist and not_private_ip. Presence syntax: `test="exist _clientIp"`; equality syntax: `test="$_decision = 'blocked'"`. Do not invent JavaScript boolean conditions; nest documented constructs when needed.

[Choose Construct](https://docs.fortinet.com/document/fortisiem/7.6.0/user-guide/953618/choose-construct): ordered first-match conditions with optional otherwise. Use for value-based branching.

[Switch Construct](https://docs.fortinet.com/document/fortisiem/7.6.0/user-guide/324900/switch-construct): regex matching determines case entry. Use for alternate log shapes, with optional default. Do not invent programming-language case-value attributes.

## Extraction

[Collect and Set Functions](https://docs.fortinet.com/document/fortisiem/7.6.0/user-guide/956470/collect-and-set-functions): `collectAndSetAttrByJSON` maps JSON paths through `attrKeyMap`; dotted paths access nested objects. Array functions have separate semantics; verify rather than assume generic JSONPath compatibility. Regex captures use `<target:patternName>` in CDATA. An empty target references a pattern without storing the match.

Example authored for this skill:

```xml
<collectAndSetAttrByJSON src="$_json">
  <attrKeyMap attr="_clientIp" key="client_ip"/>
  <attrKeyMap attr="_decision" key="decision"/>
</collectAndSetAttrByJSON>
```

## Time

[Conversions Functions](https://docs.fortinet.com/document/fortisiem/7.6.0/user-guide/962586/conversions-functions): `toDateTime` takes month, day, optional year, time and optional timezone. Documented time is HH:MM:SS, with Z/UTC/GMT or signed zone offsets. Omitted timezone uses server local timezone. Examples return epoch seconds. `toUnixTime` is for LDAP/AD GeneralizedTime, not arbitrary ISO-8601.

CSV DATE descriptions mention millisecond storage. Storage representation does not establish parser input units: do not multiply by 1,000 merely on that basis. Check fractional precision/runtime conversion. For `.74Z`, isolate fraction and zone correctly. If using second-resolution conversion, disclose lost precision instead of inventing a function. Do not equate receive time and device event time.

## Configure and activate

[Working with Event Attributes](https://docs.fortinet.com/document/fortisiem/7.6.0/user-guide/42752/working-with-event-attributes): add absent names in Admin → Device Support → Event Attributes → +. Name, Display Name and Value Type are required; Display Format/Description describe units/meaning. Save, then Apply selected new attributes.

[Working with Parsers](https://docs.fortinet.com/document/fortisiem/7.6.0/user-guide/908229/working-with-parsers): create at the appropriate list position, select Device Type, enter definition/test logs, Validate syntax, then Test outputs and parser selection. Inspect Used Parser. Enable/Save after success, then Apply. Ordering is top to bottom; broad earlier recognizers can capture samples. Device Type is a UI configuration, not an invented wrapper. Attribute inventory does not establish existing Device Types/Event Types.
