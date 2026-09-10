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

## Colour reference

`palette.svg` is the working swatch sheet — twelve roles in both renderings,
each chip flat and 100% opacity so Affinity's eyedropper picks the exact value.
Hex and RGB are printed beside every chip, and an "in context" band shows the
tokens doing their real jobs.

It is **generated**, not hand-drawn. `_sass/_deep-field.scss` is the source of
truth; regenerate after any token change rather than editing the SVG:

```bash
python3 bin/gen-palette-svg.py
```

The script also prints the contrast ratios it did not have to guess at, so an
edit that breaks AA is visible at the point you make it.

Note that `Palette.dc.html` is *not* this. That artboard shows the warm-paper
"Field Notes" exploration, which was not the direction shipped — keep it for
reference, but match colours from `palette.svg`.

## Editing a chart SVG in Affinity

Charts under `assets/images/` carry their colour as CSS custom properties — a
`svg { --competence: … }` block for light, a `@media (prefers-color-scheme:
dark)` block for dark. Browsers resolve both, which is how one file serves two
renderings.

**Affinity cannot open these as-is.** Its SVG importer parses the class rules
but implements no custom properties, so every `var()` reference collapses —
to black inside a class rule, to no paint at all in a presentation attribute
like `fill="var(--surface)"`. The graphic imports monotone on a transparent
ground. Nothing is wrong with the file; there is simply no colour in the place
Affinity looks. A static editor also has no theme, so the media query could
never apply either way.

Flatten it first. This resolves the variables to literals and drops the media
query, writing one file per theme:

```bash
python3 bin/flatten-svg-vars.py assets/images/dreyfus-confidence-competence.svg
```

That writes `_design/<name>-light.svg` and `_design/<name>-dark.svg`, and
prints the resolved palette for each so the values are checkable against
`palette.svg` without opening anything.

The flattened copies are **working copies for editing, not build inputs** — the
var-based file under `assets/images/` stays the one the site serves. If an edit
is meant to ship, port the change back into that file, or re-export from the
`.af` source below. The script takes several files at once and a `--out-dir`,
so it covers any future chart built the same way.

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
