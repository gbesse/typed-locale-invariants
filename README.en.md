# typed-locale-invariants

Finds typed decisions that flip across FR/EN/ES variants and option orders.

[Français](README.md) · [English](README.en.md) · [Español](README.es.md)

## Related projects

- [AnyJev #6 — request for multilingual evaluation](https://github.com/nokia-applied-research/AnyJev/issues/6)
- [zero-shot-ie-bench — adjacent multilingual evaluation](https://github.com/umstek/zero-shot-ie-bench)
- [jev-banc-francais — adjacent French benchmark](https://github.com/gbesse/jev-banc-francais)

These projects document the need or cover part of the problem. No affiliation or integration with them is claimed.

## Quick start

```bash
python3 tool.py demo
python3 tool.py check examples/decisions.json
```

Python 3.11+; no external package required. / Python 3.11+ ; aucune dépendance externe. / Python 3.11+; sin dependencias externas.

## Current scope

Humans author FR/EN/ES variants and link them with semantic option IDs. The check detects choice and probability changes, including under option permutation. Text equivalence still needs human review.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT.
