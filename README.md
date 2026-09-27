# typed-locale-invariants

Repère les décisions typées qui changent entre variantes FR/EN/ES et permutations d’options.

[Français](README.md) · [English](README.en.md) · [Español](README.es.md)

## Projets voisins

- [AnyJev #6 — demande d’évaluation multilingue](https://github.com/nokia-applied-research/AnyJev/issues/6)
- [zero-shot-ie-bench — évaluation multilingue voisine](https://github.com/umstek/zero-shot-ie-bench)
- [jev-banc-francais — benchmark francophone voisin](https://github.com/gbesse/jev-banc-francais)

Ces projets documentent le besoin ou couvrent une partie du problème. Aucun lien d’affiliation ni intégration avec eux n’est revendiqué.

## Démarrer

```bash
python3 tool.py demo
python3 tool.py check examples/decisions.json
```

Python 3.11+; no external package required. / Python 3.11+ ; aucune dépendance externe. / Python 3.11+; sin dependencias externas.

## Portée actuelle

Les variantes FR/EN/ES sont rédigées par des humains et liées par identifiants d’options sémantiques. Le contrôle repère les changements de choix et de probabilité, y compris sous permutation des options. L’équivalence des textes reste à valider humainement.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Licence

MIT.
