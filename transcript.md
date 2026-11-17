# Human-readable build log

This is a build narrative, not an exported provider-usage transcript or a fabricated harness session.

1. Read the kit rules, source notice, Python starter, competition configuration and practice case structure. Confirmed sparse hourly observations, first-hour anchoring, log pinball scoring, offline limits and transcript obligations.
2. Wrote main.py version 1 in an assistant write message. Extracted launch-day hours by UTC offsets, skipped missing observations and non-launch GTA VI history, excluded the target by name, computed empirical log-ratio quantiles, and smoothed across neighbours. Added sparse-sample fallback, positive rounding and output limits.
3. Wrote the external validation script. Built 37 synthetic cases, removed each target from its comparables and stripped target history. Executed the model and starter over identical inputs. Scored 851 hours: version 1 loss 0.713034 versus baseline 0.929650; typical miss 186.91% versus 213.32%; coverage 86.37% versus 62.40%. Four practice cases produced valid, byte-identical outputs across two executions.
4. In a separate later assistant message, revised main.py to use 2.5/97.5 empirical tail percentiles while preserving quartiles and medians. Motivation: first-version coverage was below nominal and late-unlock launches exceeded the upper tail. Full rerun: revised loss 0.715832 versus 0.929650; typical miss 186.91% versus 213.32%; coverage 91.07% versus 62.40%. Accepted the small pinball cost for better coverage; no claim that revision improved loss. All practice outputs remained valid and byte-identical. Runtime 0.093–0.096 seconds/case on local Python 3.12.3, not the grader's 3.13.
5. Copied starter/LICENSE verbatim and wrote README.md with exact badges, usage, results and limitations.

## Revised per-launch loss

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


## Handoff

Only main.py, LICENSE, README.md and this log belong in the repository. Validation artifacts are outside it. No network calls, purchases, credential access, GitHub creation, submissions or makefun bundle/check/submit commands were used. No real practice answers were accessed. Final-house-AI performance is unknown. Preserve genuine recorded harness transcripts and the required run record separately; this narrative alone does not satisfy that gate. Session timestamps must satisfy the opening window; no timestamps or usage have been invented here.
