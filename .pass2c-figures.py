#!/usr/bin/env python3
"""Pass 2c — generate the 2 final figures (fig 1.2 pull quote, fig 1.4 timeline)
that were missed: fig 1.2 was a CALLOUT BOX comment (token not in the spec's literal
list) and fig 1.4's TIMELINE comment was concatenated onto the previous figure label.
"""
import re
from pathlib import Path
import cairosvg

ROOT = Path(__file__).parent
CH = ROOT / "chapters"
IMG = ROOT / "images"

INK = "#1a1714"
GRAY_DARK = "#4a4540"
GRAY_MID = "#8a8480"
GRAY_LIGHT = "#c8c4c0"
CREAM = "#f5f2ee"
WHITE = "#fdfcfb"
SERIF = "Georgia, 'Times New Roman', serif"

DEFS = """<defs>
  <marker id="arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
    <polygon points="0 0, 8 3, 0 6" fill="#1a1714"/>
  </marker>
</defs>"""


def fig_1_2():
    """Pull-quote rendered as a typographic block."""
    w, h = 700, 360
    out = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">', DEFS,
           f'<rect x="0" y="0" width="{w}" height="{h}" fill="{WHITE}"/>']
    # Card
    out.append(f'<rect x="60" y="60" width="580" height="240" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    # Big quote mark
    out.append(f'<text x="100" y="150" font-family="{SERIF}" font-size="80" fill="{GRAY_LIGHT}">&#8220;</text>')
    # Quote body — wrap manually
    quote_lines = [
        "56% is not a rounding error.",
        "It is a peer-reviewed, randomized",
        "controlled experiment on professional",
        "developers doing real work.",
    ]
    for i, line in enumerate(quote_lines):
        out.append(f'<text x="350" y="{132+i*32}" font-family="{SERIF}" font-size="18" fill="{INK}" text-anchor="middle">{line}</text>')
    # Attribution rule
    out.append(f'<line x1="296" y1="270" x2="404" y2="270" stroke="{GRAY_DARK}" stroke-width="0.75"/>')
    out.append(f'<text x="350" y="288" font-family="{SERIF}" font-size="11" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">on the Peng et al. (2023) Copilot study</text>')
    out.append(f'<text x="{w/2}" y="334" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The number is the brake-line on the Spence pivot. Sit with it before the argument starts.</text>')
    out.append('</svg>')
    return "\n".join(out)


def fig_1_4():
    """Timeline 2004-2024 — disruption events that collapsed the GitHub signal."""
    w, h = 700, 360
    out = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">', DEFS,
           f'<rect x="0" y="0" width="{w}" height="{h}" fill="{WHITE}"/>']
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The compression of the signal collapse, 2004&#8211;2024</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">From signal-creation to signal-pooling in the span of a single career.</text>')

    axis_y = 200
    x0, x1 = 80, 620
    out.append(f'<line x1="{x0}" y1="{axis_y}" x2="{x1}" y2="{axis_y}" stroke="{INK}" stroke-width="1.5"/>')
    out.append(f'<path d="M{x1-6} {axis_y-4} L{x1+2} {axis_y} L{x1-6} {axis_y+4} Z" fill="{INK}"/>')

    # Years
    span = 20  # 2004 to 2024
    for year in [2004, 2008, 2012, 2016, 2020, 2024]:
        x = x0 + (year - 2004) / span * (x1 - x0)
        out.append(f'<line x1="{x}" y1="{axis_y-3}" x2="{x}" y2="{axis_y+3}" stroke="{GRAY_DARK}" stroke-width="0.75"/>')
        out.append(f'<text x="{x}" y="{axis_y+18}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">{year}</text>')

    events = [
        (2008, "GitHub launches", "build = a separating signal", -1),
        (2021, "GitHub Copilot launches", "build assistance at scale", +1),
        (2022, "Peng et al. study", "56% completion-time reduction", -1),
        (2024, "Stack Overflow survey", "82% of devs use AI tooling", +1),
    ]
    for year, l1, l2, side in events:
        x = x0 + (year - 2004) / span * (x1 - x0)
        out.append(f'<circle cx="{x}" cy="{axis_y}" r="5" fill="{INK}"/>')
        if side == -1:
            # above
            out.append(f'<line x1="{x}" y1="{axis_y-6}" x2="{x}" y2="{axis_y-46}" stroke="{GRAY_MID}" stroke-width="0.75"/>')
            out.append(f'<text x="{x}" y="{axis_y-92}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">{year}</text>')
            out.append(f'<text x="{x}" y="{axis_y-76}" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">{l1}</text>')
            out.append(f'<text x="{x}" y="{axis_y-60}" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">{l2}</text>')
        else:
            # below
            out.append(f'<line x1="{x}" y1="{axis_y+6}" x2="{x}" y2="{axis_y+46}" stroke="{GRAY_MID}" stroke-width="0.75"/>')
            out.append(f'<text x="{x}" y="{axis_y+62}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">{year}</text>')
            out.append(f'<text x="{x}" y="{axis_y+76}" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">{l1}</text>')
            out.append(f'<text x="{x}" y="{axis_y+90}" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">{l2}</text>')

    out.append(f'<text x="{w/2}" y="320" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">Thirteen years from launch to mass adoption to peer-reviewed signal collapse.</text>')
    out.append(f'<text x="{w/2}" y="340" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Most readers&#8217; careers will outlast at least one more cycle of this length.</text>')
    out.append('</svg>')
    return "\n".join(out)


def write_pair(slug, svg_str):
    svg_path = IMG / f"{slug}.svg"
    png_path = IMG / f"{slug}.png"
    svg_path.write_text(svg_str)
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg_str)
    vw, vh = int(m.group(1)), int(m.group(2))
    cairosvg.svg2png(bytestring=svg_str.encode('utf-8'),
                      output_width=vw*2, output_height=vh*2,
                      write_to=str(png_path))


# Generate
write_pair("01-the-creative-engineer-fig-02", fig_1_2())
write_pair("01-the-creative-engineer-fig-04", fig_1_4())

# Now fix chapter 01 — replace .jpg refs with .png, and clean up the merged TIMELINE line
ch01 = CH / "01-the-creative-engineer.md"
text = ch01.read_text()

# Fig 1.2 — replace the existing image markdown + remove the CALLOUT BOX comment above it
text = re.sub(
    r'<!--\s*→\s*\[CALLOUT BOX:[^\n]*?-->\s*\n+'
    r'!\[[^\]]*\]\(images/01-the-creative-engineer-fig-02\.jpg\)',
    '![Pull quote rendered as a typographic block — \"56% is not a rounding error. It is a peer-reviewed, randomized controlled experiment on professional developers doing real work.\"](images/01-the-creative-engineer-fig-02.png)\n*Figure 1.2 — The number that anchors the chapter*',
    text, count=1,
)

# Fig 1.4 — the TIMELINE comment was concatenated onto Figure 1.3's caption line
# Pattern: "*Figure 1.3 — Separating vs. pooling equilibrium*<!-- TIMELINE comment -->"
# We want: "*Figure 1.3 — Separating vs. pooling equilibrium*\n\n[new fig 1.4 image]"
# Then remove the existing fig-04.jpg image markdown that follows.
text = re.sub(
    r'(\*Figure 1\.3 — [^*]+\*)\s*<!--\s*→\s*\[TIMELINE:[^\n]*?-->\s*\n+'
    r'!\[[^\]]*\]\(images/01-the-creative-engineer-fig-04\.jpg\)',
    r'\1\n\n![Horizontal timeline of the GitHub signal collapse, 2004 to 2024 — GitHub launches, Copilot launches, Peng et al. study, Stack Overflow 82% survey](images/01-the-creative-engineer-fig-04.png)\n*Figure 1.4 — The compression of the signal collapse*',
    text, count=1,
)

ch01.write_text(text)
print("ch01 updated; verifying remaining .jpg refs:")
remaining = re.findall(r'!\[[^\]]*\]\(images/[^)]+\.jpg\)', text)
for r in remaining:
    print(f"  {r[:120]}")
print(f"  total remaining .jpg image refs: {len(remaining)}")
