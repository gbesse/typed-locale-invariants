"""Check semantic choice stability across human-authored locale variants."""
import json
import sys
from pathlib import Path

REQUIRED_LOCALES = {'fr', 'en', 'es'}


def check(data):
    findings = []
    details = []
    threshold = data.get('max_probability_drift', 0.15)
    for group in data['groups']:
        variants = group['variants']
        locales = {v['locale'] for v in variants}
        if locales != REQUIRED_LOCALES:
            raise ValueError(f'{group["id"]}: expected exactly FR/EN/ES locales')
        choices = []
        probabilities = []
        for variant in variants:
            ids = variant['option_ids']
            if len(ids) != len(set(ids)) or variant['choice'] not in ids:
                raise ValueError(f'{group["id"]}: invalid semantic option ID')
            choices.append(variant['choice'])
            probabilities.append(variant['probability'])
        flipped = len(set(choices)) > 1
        order_flips = sorted({v['locale'] for v in variants if len({w['choice'] for w in variants if w['locale'] == v['locale']}) > 1})
        drift = max(probabilities) - min(probabilities)
        if flipped:
            findings.append(f'{group["id"]}: semantic choice flips across variants')
        if order_flips:
            findings.append(f'{group["id"]}: option-order flip within locales {order_flips}')
        if drift > threshold:
            findings.append(f'{group["id"]}: probability drift {drift:.3f} exceeds {threshold:.3f}')
        details.append({'id': group['id'], 'choices': choices, 'option_order_flips': order_flips, 'probability_drift': round(drift, 4)})
    return {'ok': not findings, 'groups': details, 'findings': findings}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('demo', 'check'):
        raise SystemExit('usage: tool.py demo | check DECISIONS.json')
    path = Path(__file__).parent/'examples/decisions.json' if sys.argv[1] == 'demo' else Path(sys.argv[2])
    result = check(json.loads(path.read_text()))
    print(json.dumps(result, indent=2))
    return 0 if sys.argv[1] == 'demo' or result['ok'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
