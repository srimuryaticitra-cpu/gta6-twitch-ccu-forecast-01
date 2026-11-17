# GTA VI Twitch hourly CCU forecaster

[![make.fun · gta6-twitch-ccu-forecast-01](https://make.fun/badge/gta6-twitch-ccu-forecast-01.svg)](https://make.fun/bounty/gta6-twitch-ccu-forecast-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-twitch-ccu-forecast-01)
[![rank](https://make.fun/badge/gta6-twitch-ccu-forecast-01/srimuryaticitra-cpu/gta6-twitch-ccu-forecast-01/rank.svg)](https://make.fun/bounty/gta6-twitch-ccu-forecast-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-twitch-ccu-forecast-01)
[![reward](https://make.fun/badge/gta6-twitch-ccu-forecast-01/srimuryaticitra-cpu/gta6-twitch-ccu-forecast-01/reward.svg)](https://make.fun/bounty/gta6-twitch-ccu-forecast-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-twitch-ccu-forecast-01)

Given the observed hour-1 viewer count, `main.py` estimates Twitch concurrent viewers for the remaining launch-day hours. Execution is deterministic, requires only the Python standard library, and makes no network requests.

The prior describes launch shapes using log-ratios: for each comparable launch, hour-h viewers are divided by that launch's hour-1 viewers before taking the logarithm. Pooling these observations lets the forecast borrow relative growth and decline patterns while retaining the target's observed starting scale. Quantiles are smoothed across neighbouring hours. Thin hourly samples first borrow observations from nearby hours; if those remain insufficient, the model uses persistence with uncertainty that widens over time. The target game's own curve and GTA VI pre-launch category history are excluded.

## Execution and output

Set the input and output directories, then run the program:

```sh
export MAKEFUN_INPUT_DIR=/path/to/input
export MAKEFUN_OUTPUT_DIR=/path/to/output
python3 main.py
```

Without these environment variables, the directories are `/input` and `/output`. Input files matching `*.in` are read in sorted order, and each produces a matching `.out` filename. Every output covers hours 2-24 with five positive, nondecreasing quantiles per hour. Values are capped at 1e9 and rounded half-up to two decimals, with a minimum of 0.01.

Python 3.13 is the target interpreter. Local checks used Python 3.12.3.

## Evidence from local checks

Leave-one-out validation treated each of 37 comparable launches as a synthetic target, removing its own curve from the available comparables. Across 851 scored hours, the revised model and starter baseline obtained:

| Measure | Revised forecast | Starter baseline |
|---|---:|---:|
| Mean log pinball loss | 0.715832 | 0.929650 |
| Typical miss | 186.91% | 213.32% |
| 90% coverage | 91.07% | 62.40% |

The first version had loss 0.713034 and coverage 86.37%. To improve coverage, the revision moved the empirical tails from the 5/95 to the 2.5/97.5 percentiles, retaining the quartiles and median. The wider tails increased coverage at a small pinball cost.

All four real practice cases passed schema checks, and their outputs were byte-identical across two runs. Runtime was about 0.09 seconds per case; the recorded local range was 0.093-0.096 seconds on Python 3.12.3.

These scores measure performance on comparables, not the house's practice answers. They say nothing about performance against the house AI; the final is a live race. The per-launch measurements and development history are recorded in [transcript.md](transcript.md).
