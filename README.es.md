# typed-locale-invariants

Detecta decisiones tipadas que cambian entre variantes FR/EN/ES y órdenes de opciones.

[Français](README.md) · [English](README.en.md) · [Español](README.es.md)

## Proyectos relacionados

- [AnyJev #6 — solicitud de evaluación multilingüe](https://github.com/nokia-applied-research/AnyJev/issues/6)
- [zero-shot-ie-bench — evaluación multilingüe cercana](https://github.com/umstek/zero-shot-ie-bench)
- [jev-banc-francais — benchmark francés cercano](https://github.com/gbesse/jev-banc-francais)

Estos proyectos documentan la necesidad o cubren parte del problema. No se afirma ninguna afiliación ni integración con ellos.

## Inicio rápido

```bash
python3 tool.py demo
python3 tool.py check examples/decisions.json
```

Python 3.11+; no external package required. / Python 3.11+ ; aucune dépendance externe. / Python 3.11+; sin dependencias externas.

## Alcance actual

Personas redactan variantes FR/EN/ES y las vinculan mediante ID de opciones semánticas. El control detecta cambios de elección y probabilidad, también al permutar opciones. La equivalencia de los textos requiere revisión humana.

## Pruebas

```bash
python3 -m unittest discover -s tests -v
```

## Licencia

MIT.
