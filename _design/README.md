# Design sources

Working files for the **Deep Field** redesign — the visual spec the site was
built from. Nothing in here is rendered: `_design` is excluded in `_config.yml`,
and Jekyll ignores `_`-prefixed directories anyway.

## What these are

Each `.dc.html` is one artboard — a self-contained page mockup. `canvas.json`
lays them out on a pan/zoom canvas and groups them into pages.

| file | what it shows |
| --- | --- |
| `Main.dc.html` | Deep Field post page, dark — the chosen direction |
| `DeepFieldHome.dc.html` / `DeepFieldArchive.dc.html` | home and archive, dark |
| `DeepFieldLightPost.dc.html` / `DeepFieldLightHome.dc.html` | the light rendering |
| `Topics.dc.html` | the flat, unranked topic index |
| `Palette.dc.html` / `Typography.dc.html` | colour and type foundations |
| `QuoteStudies.dc.html` | three pull-quote treatments; "tinted panel" was chosen |
| `FieldNotes*.dc.html` | the direction that was **not** chosen, kept for reference |

## Affinity sources

The `.af` files are Affinity Designer documents — the vector sources for
hand-made post graphics, exported to SVG/PNG under `assets/images/`.

| file | for |
| --- | --- |
| `razor_header.af` | header art for the Hanlon's razor post |
| `dreyfus-confidence-competence.af` | Dreyfus confidence/competence graphic |

Keep these here rather than in `_drafts/`. Jekyll parses *every* file in
`_drafts/` as a document and dies on binary with "invalid byte sequence in
UTF-8" — and only under `--drafts`, so a plain `jekyll build` looks fine while
local preview is broken. Affinity's `*~lock~` files are gitignored.

## Live canvas

https://claude.ai/code/artifact/1d72cba9-bef1-443a-8f64-44bb96814679

The published canvas is the easiest way to view these — it renders every
artboard side by side and exports PNG/PDF.

## Why the seeded HTML is not committed

Publishing bundles these sources into a single ~2.5 MB HTML file containing the
canvas editor. That file is build output: it is gitignored, and it can be
regenerated from these sources, or pulled back down from the artifact above.

## Where the design actually lives now

The implementation is in `_sass/_deep-field.scss` (tokens, both renderings and
every component), with layout in `_layouts/` and `_includes/`. If the two ever
disagree, the stylesheet wins — these files are the intent, not the source of
truth.
