# Development record and handoff

This account restates the recorded build history and measurements. The documentation refresh did not repeat those experiments or change the finished program. It is a readable log, not a recorded harness transcript.

1. **Establish the requirements.** The build began by reading the kit rules and starter implementation, including the case format, hour-1 anchor, scoring rules and offline execution requirements.
2. **Implement the initial forecast.** Version 1 of `main.py` assigned observations to launch hours using UTC offsets from the day start. It skipped missing observations and non-launch GTA VI history, and removed the target game by name. Comparable launches supplied empirical log-ratio quantiles, which were smoothed across neighbouring hours. Sparse samples received a fallback, and output handling enforced positive rounding and the required limits.
3. **Prepare an independent validation harness.** An external script constructed 37 synthetic leave-one-out cases. Each launch became the target in turn, with its own curve removed from the comparables. The model and starter received identical cases, providing 851 scored hours.
4. **Measure version 1.** Mean log pinball loss was 0.713034, typical miss was 186.91%, and 90% coverage was 86.37%. The starter baseline scored 0.929650 / 213.32% / 62.40% for the same three measures. Coverage fell below nominal, and late-unlock launches extended beyond the estimated upper tail.
5. **Adjust the tails in a later implementation step.** `main.py` was revised to estimate empirical tails at the 2.5/97.5 percentiles instead of 5/95. Quartiles and medians retained their original percentile levels. The change addressed the observed coverage shortfall.
6. **Rerun the full comparison.** Revised loss was 0.715832, typical miss was 186.91%, and coverage was 91.07%; the baseline remained 0.929650 / 213.32% / 62.40%. The small pinball cost was accepted in exchange for better coverage.
7. **Check practice execution.** All four real practice cases produced schema-valid outputs that were byte-identical across two runs. Recorded runtime was 0.093-0.096 seconds per case on local Python 3.12.3, not the grader's Python 3.13.

The following measurements break down mean log pinball loss by held-out launch after the tail revision. There are 37 launches; the comparison column uses the starter baseline.

| Held-out launch | Revised loss | Starter loss |
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

For the submitter: the repository should contain only `main.py`, `LICENSE`, `README.md` and this log. Validation artifacts live outside it. No network calls, purchases, credentials, GitHub creation, submissions or makefun bundle/check/submit commands were used. No real practice answers were accessed, so performance against the final house AI remains unknown. Keep the genuine recorded harness transcripts separately; this rewritten account does not replace them.
