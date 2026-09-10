#!/usr/bin/env python3
"""Generate _design/palette.svg from the tokens in _sass/_deep-field.scss."""
import re, pathlib

SCSS = pathlib.Path("_sass/_deep-field.scss")
OUT  = pathlib.Path("_design/palette.svg")

src = SCSS.read_text()

# The light block is :root { ... } before the media query; dark is inside it.
light_src, dark_src = src.split("@media (prefers-color-scheme: dark)", 1)
tok = re.compile(r"--(df-[a-z0-9-]+)\s*:\s*(#[0-9a-fA-F]{6})\s*;")
light = dict(tok.findall(light_src))
dark  = dict(tok.findall(dark_src))

# Roles, in the order the stylesheet declares them.
ROLES = [
    ("df-ground",      "Ground",      "page background"),
    ("df-ground-tint", "Ground tint", "banded sections, teaser cards"),
    ("df-surface",     "Surface",     "raised panels, nav overflow"),
    ("df-text",        "Text",        "body copy"),
    ("df-text-dim",    "Text dim",    "meta, captions, secondary"),
    ("df-rule",        "Rule",        "hairlines, borders, dividers"),
    ("df-accent",      "Accent",      "prose links, primary mark"),
    ("df-accent-2",    "Accent 2",    "links-tier only, never his own writing"),
    ("df-nav",         "Nav",         "masthead links"),
    ("df-quote-bg",    "Quote bg",    "pull-quote tinted panel"),
    ("df-quote-text",  "Quote text",  "pull-quote copy"),
    ("df-quote-mark",  "Quote mark",  "pull-quote glyph"),
]

missing = [k for k, _, _ in ROLES if k not in light or k not in dark]
if missing:
    raise SystemExit(f"tokens missing from {SCSS}: {missing}")

def rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))

def lum(h):
    def ch(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

SANS = "Helvetica Neue, Helvetica, Arial, sans-serif"
MONO = "JetBrains Mono, Menlo, Consolas, monospace"

# Geometry
PAD, GUT = 40, 36
PANEL_W  = 620
ROW_H, CHIP_W, CHIP_H = 68, 128, 52
HEAD_H   = 112
SAMPLE_H = 186
PANEL_H  = HEAD_H + ROW_H * len(ROLES) + SAMPLE_H + 34
W = PAD * 2 + PANEL_W * 2 + GUT
H = 96 + PANEL_H + 74

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def text(x, y, s, size=13, fill="#000", font=SANS, weight=400,
         anchor="start", ls=None, op=None):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    l = f' letter-spacing="{ls}"' if ls else ""
    o = f' opacity="{op}"' if op else ""
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}"{a}{l}{o}>{esc(s)}</text>')

def panel(x0, y0, name, pal):
    g, txt, dim, rule = pal["df-ground"], pal["df-text"], pal["df-text-dim"], pal["df-rule"]
    o = [f'<g><rect x="{x0}" y="{y0}" width="{PANEL_W}" height="{PANEL_H}" fill="{g}"/>']
    o.append(text(x0 + 32, y0 + 46, name.upper(), 12, dim, MONO, 500, ls="0.16em"))
    o.append(text(x0 + 32, y0 + 82, "Deep Field", 30, txt,
                  "Instrument Serif, Times New Roman, Georgia, serif"))
    o.append(f'<line x1="{x0 + 32}" y1="{y0 + HEAD_H - 14}" x2="{x0 + PANEL_W - 32}" '
             f'y2="{y0 + HEAD_H - 14}" stroke="{rule}" stroke-width="1"/>')

    for i, (key, label, use) in enumerate(ROLES):
        hexv = pal[key]
        r, gg, b = rgb(hexv)
        y = y0 + HEAD_H + i * ROW_H
        cy = y + (ROW_H - CHIP_H) / 2
        o.append(f'<rect x="{x0 + 32}" y="{cy}" width="{CHIP_W}" height="{CHIP_H}" '
                 f'fill="{hexv}" stroke="{rule}" stroke-width="1"/>')
        tx = x0 + 32 + CHIP_W + 20
        o.append(text(tx, y + 26, label, 14, txt, SANS, 600))
        o.append(text(tx, y + 43, use, 11, dim, SANS))
        rx = x0 + PANEL_W - 32
        o.append(text(rx, y + 26, hexv.upper(), 13, txt, MONO, 500, anchor="end"))
        o.append(text(rx, y + 43, f"{r}, {gg}, {b}", 11, dim, MONO, anchor="end"))

    # In-context sample: the same tokens doing their actual jobs.
    sy = y0 + HEAD_H + ROW_H * len(ROLES) + 8
    o.append(f'<rect x="{x0 + 32}" y="{sy}" width="{PANEL_W - 64}" height="{SAMPLE_H - 24}" '
             f'fill="{pal["df-ground-tint"]}" stroke="{rule}" stroke-width="1"/>')
    o.append(text(x0 + 52, sy + 32, "IN CONTEXT", 10, dim, MONO, 500, ls="0.16em"))
    # tspans, not hand-placed x offsets — the run has to reflow with the font.
    o.append(f'<text x="{x0 + 52}" y="{sy + 60}" font-family="{SANS}" font-size="15" '
             f'fill="{txt}">Body copy sets over the ground, '
             f'<tspan fill="{pal["df-accent"]}" font-weight="500">a prose link</tspan>'
             f' inside it.</text>')
    o.append(text(x0 + 52, sy + 80, "Meta and captions sit dim. Nav is its own tone.",
                  12, dim, SANS))
    qy = sy + 96
    o.append(f'<rect x="{x0 + 52}" y="{qy}" width="{PANEL_W - 104}" height="{54}" '
             f'fill="{pal["df-quote-bg"]}"/>')
    o.append(f'<rect x="{x0 + 52}" y="{qy}" width="3" height="54" fill="{pal["df-accent"]}"/>')
    o.append(text(x0 + 70, qy + 30, "“", 30, pal["df-quote-mark"], "Georgia, serif"))
    o.append(text(x0 + 92, qy + 24, "The tinted panel, not a bar or a rule.",
                  13, pal["df-quote-text"], SANS))
    o.append(text(x0 + 92, qy + 43, "Accent 2 marks the links tier only.",
                  12, pal["df-accent-2"], SANS))
    o.append("</g>")
    return "\n  ".join(o)

body = [
    f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
    text(PAD, 46, "DEEP FIELD — COLOUR TOKENS", 12, "#635e75", MONO, 500, ls="0.16em"),
    text(PAD, 74, "bruceabernethy.com — generated from _sass/_deep-field.scss",
         13, "#1b1926", SANS),
    panel(PAD, 96, "Light", light),
    panel(PAD + PANEL_W + GUT, 96, "Dark", dark),
    text(PAD, H - 42,
         "Twelve roles, redefined once for dark. Eyedrop the chips — every fill is flat, "
         "100% opacity, no gradient or blend.", 12, "#635e75", SANS),
    text(PAD, H - 24,
         "Type: Instrument Serif (display) · Literata (body) · JetBrains Mono (meta). "
         "Regenerate: python3 bin/gen-palette-svg.py", 12, "#635e75", SANS),
]

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
       f'viewBox="0 0 {W} {H}">\n  <title>Deep Field colour tokens</title>\n  '
       + "\n  ".join(body) + "\n</svg>\n")

OUT.write_text(svg)

# Report the contrast pairs worth knowing while drawing.
for nm, pal in (("light", light), ("dark", dark)):
    print(nm,
          "text/ground %.2f" % contrast(pal["df-text"], pal["df-ground"]),
          "dim/ground %.2f" % contrast(pal["df-text-dim"], pal["df-ground"]),
          "accent/ground %.2f" % contrast(pal["df-accent"], pal["df-ground"]),
          "accent2/ground %.2f" % contrast(pal["df-accent-2"], pal["df-ground"]),
          "nav/ground %.2f" % contrast(pal["df-nav"], pal["df-ground"]))
print("wrote", OUT, OUT.stat().st_size, "bytes")
