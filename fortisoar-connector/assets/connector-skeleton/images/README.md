# Connector icons

FortiSOAR requires two PNG icons here, referenced by `info.json`
(`icon_small_name` / `icon_large_name`):

- `small.png` — **32×32** px, RGBA PNG
- `large.png` — **80×80** px, RGBA PNG

These are binary image assets that must be supplied by a human — Claude cannot
originate real artwork. Until you drop real PNGs in this folder, the connector will
install but show a broken/placeholder icon.

If you name your icons differently (e.g. `medium.png`), update `icon_small_name` /
`icon_large_name` in `info.json` to match.
