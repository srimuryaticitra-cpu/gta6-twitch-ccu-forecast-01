# GTA VI Twitch hourly forecast

[![make.fun · gta6-twitch-ccu-forecast-01](https://make.fun/badge/gta6-twitch-ccu-forecast-01.svg)](https://make.fun/bounty/gta6-twitch-ccu-forecast-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-twitch-ccu-forecast-01)
[![rank](https://make.fun/badge/gta6-twitch-ccu-forecast-01/srimuryaticitra-cpu/gta6-twitch-ccu-forecast-01/rank.svg)](https://make.fun/bounty/gta6-twitch-ccu-forecast-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-twitch-ccu-forecast-01)
[![reward](https://make.fun/badge/gta6-twitch-ccu-forecast-01/srimuryaticitra-cpu/gta6-twitch-ccu-forecast-01/reward.svg)](https://make.fun/bounty/gta6-twitch-ccu-forecast-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-twitch-ccu-forecast-01)

Deterministic Python standard-library forecaster anchored to the observed first UTC hour. It pools comparable launch-day log ratios, smooths neighbouring hourly quantiles, and expands empirical tails to account for limited launch samples. It excludes the target game's own curve and GTA VI pre-launch category history. Sparse samples use neighbouring hours or a widening persistence fallback. No network or external data is used.

Run with Python 3.13:

```sh
MAKEFUN_INPUT_DIR=/path/to/input MAKEFUN_OUTPUT_DIR=/path/to/output python3 -B main.py
```

Reads sorted `*.in` files and writes corresponding `.out` files; defaults are `/input` and `/output`. Outputs contain exactly hours 2–24 and five positive, ordered quantiles, capped at 1e9 and rounded half up to two decimals.

## Local validation

Leave-one-launch-out on 37 launches from p00's comparables, 851 scored hours. Each synthetic target is removed from its model input. GTA VI's category history is excluded because it is not a launch. Both programs were executed on identical synthetic files.

| Metric | Revised model | Starter baseline |
|---|---:|---:|
| Mean log pinball loss | 0.715832 | 0.929650 |
| Typical miss | 186.91% | 213.32% |
| 90% coverage | 91.07% | 62.40% |

First version: loss 0.713034, typical miss 186.91%, coverage 86.37%. Revision widened empirical tails from 5/95 to 2.5/97.5 percentiles: improved coverage, slightly worse pinball loss. The broad launch pool includes simultaneous and early-access releases; performance varies substantially by launch.

All four real practice cases passed exact output-schema checks and two-run byte equality. Revised measured process runtime: 0.093–0.096 seconds per case. Local interpreter was Python 3.12.3; Python 3.13 was not available for this check. Source uses standard-library features compatible with 3.13.

| Launch | Model loss | Baseline loss |
|---|---:|---:|
| 007 First Light | 0.431939 | 0.348392 |
| ARC Raiders | 2.100928 | 3.376581 |
| Assassin's Creed Shadows | 0.482572 | 0.345184 |
| Baldur's Gate 3 | 1.227941 | 2.176751 |
| Battlefield 6 | 1.407510 | 2.406462 |
| Black Myth: Wukong | 2.397175 | 3.434010 |
| Borderlands 4 | 0.448673 | 0.252859 |
| Call of Duty: Black Ops 6 | 0.296179 | 0.261961 |
| Call of Duty: Black Ops 7 | 0.272090 | 0.173284 |
| Call of Duty: Modern Warfare 4 | 0.267746 | 0.236143 |
| Call of Duty: Modern Warfare III | 0.290831 | 0.151954 |
| Clair Obscur: Expedition 33 | 0.628570 | 1.145018 |
| Cyberpunk 2077 | 0.465701 | 0.229932 |
| DOOM: The Dark Ages | 0.356723 | 0.256378 |
| Death Stranding 2: On the Beach | 0.294977 | 0.176153 |
| Diablo IV | 0.313880 | 0.125414 |
| ELDEN RING | 0.419070 | 0.210845 |
| Elden Ring Nightreign | 0.439816 | 0.251615 |
| FINAL FANTASY VII REBIRTH | 0.283869 | 0.173399 |
| Forza Horizon 5 | 0.385117 | 0.324841 |
| Forza Horizon 6 | 0.313569 | 0.409804 |
| Ghost of Tsushima | 0.260194 | 0.228260 |
| Ghost of Yōtei | 0.358168 | 0.473394 |
| HELLDIVERS 2 | 2.057488 | 3.428756 |
| Halo Infinite | 0.579798 | 0.631351 |
| Hogwarts Legacy | 0.379806 | 0.288149 |
| Hollow Knight: Silksong | 2.629858 | 3.941057 |
| Kingdom Come: Deliverance II | 2.218742 | 3.463761 |
| Marathon | 0.992845 | 1.745241 |
| Marvel Rivals | 0.450713 | 0.209714 |
| Monster Hunter Wilds | 0.391029 | 0.427325 |
| Resident Evil Requiem | 0.756371 | 1.272900 |
| Saros | 0.358797 | 0.601135 |
| Starfield | 0.572409 | 0.290939 |
| Stellar Blade | 0.304643 | 0.372453 |
| The Last of Us Part II | 0.346799 | 0.246974 |
| The Legend of Zelda: Tears of the Kingdom | 0.303233 | 0.308675 |


Validation code and detailed before/after JSON reports are outside this repository in `../hidden_files/gta6-validation/`. Run `python3 -B ../hidden_files/gta6-validation/validate.py rerun.json` in this workspace to reproduce.

Real practice answers are unavailable locally. These results are on comparables, not the house's four practice answers, and do not establish performance against the house AI. The final is a live race. This repository has not been submitted, bundled, or checked with makefun. A human-readable build log is not a substitute for the harness-recorded session transcripts and run record required for entry; preserve those separately. Verify the session opening time and transcript requirements before any future submission.
