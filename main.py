"""Offline launch-day empirical log-ratio quantile forecaster."""
import json
import math
import os
from datetime import datetime
from pathlib import Path

LEVELS = (0.05, 0.25, 0.5, 0.75, 0.95)
Z = (-1.645, -0.674, 0.0, 0.674, 1.645)
# Small cross-launch samples underestimate tail risk, especially late unlocks.
# Expand only the empirical tails; retain the central shape estimates.
EMPIRICAL_LEVELS = (0.025, 0.25, 0.5, 0.75, 0.975)


def stamp(s):
    return datetime.fromisoformat(s.replace('Z', '+00:00'))


def launch_hours(launch):
    start = stamp(launch['day_start'])
    buckets = {}
    for row in launch.get('hourly', []):
        offset = (stamp(row['from']) - start).total_seconds() / 3600
        if 0 <= offset < 24 and row.get('viewers') is not None:
            buckets.setdefault(int(offset) + 1, []).append(max(1, row['viewers']))
    return {h: sum(v) / len(v) for h, v in sorted(buckets.items())}


def quantile(values, tau):
    values = sorted(values)
    pos = (len(values) - 1) * tau
    i = int(pos)
    return values[i] + (values[min(i + 1, len(values) - 1)] - values[i]) * (pos - i)


def forecast_case(case):
    first = next((r for r in case.get('known', []) if r.get('hour') == 1), None)
    if first is None or first.get('viewers') is None:
        raise ValueError('Case has no hour-1 viewers print')
    p1 = max(1, first['viewers'])
    samples = {h: [] for h in range(2, 25)}
    for launch in sorted(case.get('comparables', []), key=lambda x: (x['name'], x['day_start'])):
        name = launch['name'].casefold()
        if name == case['game']['name'].casefold() or 'grand theft auto vi' in name or 'not a launch' in launch.get('unlock', '').casefold():
            continue
        hours = launch_hours(launch)
        if 1 not in hours:
            continue
        for h in samples:
            if h in hours:
                samples[h].append(math.log(hours[h] / hours[1]))
    raw = {}
    for h in samples:
        pool = samples[h]
        if len(pool) < 5:
            pool = [v for k in range(max(2, h - 2), min(24, h + 2) + 1) for v in samples[k]]
        raw[h] = [quantile(pool, t) for t in EMPIRICAL_LEVELS] if len(pool) >= 5 else [z * 0.15 * math.sqrt(h - 1) for z in Z]
    rows = []
    for h in range(2, 25):
        neighbours = [(k, 2 if k == h else 1) for k in range(max(2, h - 1), min(24, h + 1) + 1)]
        logs = [sum(raw[k][j] * w for k, w in neighbours) / sum(w for k, w in neighbours) for j in range(5)]
        qs = []
        for value in logs:
            x = min(1e9, math.exp(min(math.log(1e9), math.log(p1) + value)))
            rounded = max(0.01, math.floor(x * 100 + 0.5) / 100)
            qs.append(max(qs[-1] if qs else 0.01, rounded))
        rows.append({'hour': h, 'q': qs})
    return {'hours': rows}


def main():
    source = Path(os.environ.get('MAKEFUN_INPUT_DIR', '/input'))
    dest = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'))
    dest.mkdir(parents=True, exist_ok=True)
    for path in sorted(source.glob('*.in')):
        case = json.loads(path.read_text(encoding='utf-8'))
        result = forecast_case(case)
        (dest / (path.stem + '.out')).write_text(json.dumps(result, separators=(',', ':'), allow_nan=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
