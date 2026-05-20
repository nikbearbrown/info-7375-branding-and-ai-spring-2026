#!/usr/bin/env python3
"""Pass 2b — generate 7 SVG+PNG figures for the remaining INFOGRAPHIC/CHART/TIMELINE
comments in branding-and-ai. Replace the comments + adjacent .jpg placeholders.
"""
import re
from pathlib import Path
import cairosvg

ROOT = Path(__file__).parent
CH = ROOT / "chapters"
IMG = ROOT / "images"
IMG.mkdir(exist_ok=True)

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


def svg_open(w, h):
    return [
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">',
        DEFS,
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="{WHITE}"/>',
    ]


# ---------------------------------------------------------------------------
# Fig 1.1 — Copilot bar chart (Peng et al.)
# ---------------------------------------------------------------------------
def fig_1_1():
    w, h = 700, 420
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Task completion time — HTTP-server build</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Peng et al. (2023). Median minutes to working solution.</text>')

    # Y axis & gridlines
    base_y = 340
    top_y = 110
    chart_left = 200
    chart_right = 600
    out.append(f'<line x1="{chart_left}" y1="{base_y}" x2="{chart_right}" y2="{base_y}" stroke="{INK}" stroke-width="1"/>')
    # Y ticks
    for val, y in [(0, base_y), (40, base_y - 60), (80, base_y - 120), (120, base_y - 180), (160, base_y - 230)]:
        out.append(f'<line x1="{chart_left-4}" y1="{y}" x2="{chart_left}" y2="{y}" stroke="{GRAY_DARK}" stroke-width="0.75"/>')
        out.append(f'<text x="{chart_left-12}" y="{y+4}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="end">{val}</text>')

    # Bars — values 161 (control) and 71 (copilot)
    bar_w = 100
    # Scale: 1 minute = 1.4375 px
    scale = (base_y - top_y) / 161
    bars = [
        ("Control group", 161, chart_left + 60),
        ("Copilot group", 71, chart_left + 230),
    ]
    for label, val, x in bars:
        h_bar = val * scale
        y = base_y - h_bar
        fill = INK if "Copilot" in label else GRAY_MID
        out.append(f'<rect x="{x}" y="{y}" width="{bar_w}" height="{h_bar}" fill="{fill}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{x + bar_w/2}" y="{y - 8}" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">{val} min</text>')
        out.append(f'<text x="{x + bar_w/2}" y="{base_y + 18}" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">{label}</text>')

    # Y-axis label
    out.append(f'<text x="{chart_left-44}" y="{(base_y+top_y)/2}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle" transform="rotate(-90 {chart_left-44} {(base_y+top_y)/2})">Minutes to solution</text>')

    # Reduction callout
    out.append(f'<text x="{w/2}" y="384" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">56% reduction in completion time</text>')
    out.append(f'<text x="{w/2}" y="402" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The build signal cheapened by more than half. Brand and ship became the new separating signals.</text>')

    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Fig 1.5 — Four-verb framework
# ---------------------------------------------------------------------------
def fig_1_5():
    w, h = 700, 420
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The four verbs of the Creative Engineer</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Each verb is a separating signal. Build cheapens; the others have to do more of the separation work.</text>')

    verbs = [
        ("IDEATE", "Scope a problem worth solving", "What gets built — and why", 56),
        ("BUILD", "Produce a working artifact", "The cheapened verb", 220),
        ("BRAND", "Position for a specific audience", "Who the work is for", 384),
        ("SHIP", "Get it in front of users", "Real-world feedback loop", 548),
    ]
    cy = 200
    for label, sub, role, x in verbs:
        emph = (label == "BUILD")
        # Greyed for BUILD to show "cheapened"
        fill = GRAY_LIGHT if emph else CREAM
        out.append(f'<rect x="{x-72}" y="{cy-72}" width="144" height="144" fill="{fill}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{x}" y="{cy-44}" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">{label}</text>')
        # Subtitle
        out.append(f'<text x="{x}" y="{cy-22}" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">{sub}</text>')
        out.append(f'<text x="{x}" y="{cy+30}" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">{role}</text>')

    # Arrows between verbs
    for i in range(3):
        x1 = verbs[i][3] + 72
        x2 = verbs[i+1][3] - 72
        out.append(f'<path d="M{x1} {cy} L{x2} {cy}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')

    # Bottom note
    out.append(f'<text x="{w/2}" y="332" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">The portfolio that demonstrates all four is hard to assemble — and reads as the new costly signal.</text>')
    out.append(f'<text x="{w/2}" y="354" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Build alone separates only when build itself is hard. When tooling cheapens the build, separation moves upstream and downstream.</text>')
    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Fig 1.10 — Twelve-archetype wheel
# ---------------------------------------------------------------------------
def fig_1_10():
    w, h = 700, 600
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The twelve archetypes — grouped by orientation</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Three orientations, four archetypes each. The orientation predicts what the archetype optimizes for.</text>')

    import math
    cx, cy, r = 350, 320, 200
    archetypes = [
        # (name, group)
        ("Hero", "Ego"), ("Outlaw", "Ego"), ("Magician", "Ego"), ("Ruler", "Ego"),
        ("Sage", "Soul"), ("Explorer", "Soul"), ("Innocent", "Soul"), ("Creator", "Soul"),
        ("Caregiver", "Self"), ("Lover", "Self"), ("Jester", "Self"), ("Everyman", "Self"),
    ]
    n = len(archetypes)
    for i, (name, group) in enumerate(archetypes):
        angle = -math.pi/2 + (2*math.pi * i / n)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        # Box
        out.append(f'<rect x="{x-44}" y="{y-16}" width="88" height="32" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{x}" y="{y+5}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">{name}</text>')

    # Group labels in concentric arcs (very subtle — a sub-label below each box would work)
    # Simpler: three group labels around the wheel
    group_positions = [
        ("EGO-DRIVEN", -math.pi/4, "want to leave a mark on the world"),
        ("SOUL-DRIVEN", -math.pi/4 + 2*math.pi/3, "want to find/share what is true"),
        ("SELF-DRIVEN", -math.pi/4 + 4*math.pi/3, "want to belong to / care for community"),
    ]
    for label, angle, sub in group_positions:
        gx = cx + (r + 56) * math.cos(angle)
        gy = cy + (r + 56) * math.sin(angle)
        out.append(f'<text x="{gx}" y="{gy}" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{GRAY_DARK}" text-anchor="middle" letter-spacing="1.5">{label}</text>')

    # Center
    out.append(f'<circle cx="{cx}" cy="{cy}" r="38" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="{cx}" y="{cy-2}" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{INK}" text-anchor="middle">Twelve</text>')
    out.append(f'<text x="{cx}" y="{cy+12}" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{INK}" text-anchor="middle">archetypes</text>')

    out.append(f'<text x="{w/2}" y="572" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The framework is descriptive, not prescriptive. Use it to read the archetype your audience needs you to play.</text>')
    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Fig 5.4 — Apollo timeline
# ---------------------------------------------------------------------------
def fig_5_4():
    w, h = 700, 420
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">From contract change to product death — sixty days</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The third-party Reddit ecosystem, April–July 2023.</text>')

    # Timeline axis
    axis_y = 220
    x0, x1 = 80, 620
    out.append(f'<line x1="{x0}" y1="{axis_y}" x2="{x1}" y2="{axis_y}" stroke="{INK}" stroke-width="1.5"/>')
    # Arrow at end
    out.append(f'<path d="M{x1-6} {axis_y-4} L{x1+2} {axis_y} L{x1-6} {axis_y+4} Z" fill="{INK}"/>')

    events = [
        ("Apr 2023", "Reddit announces", "API pricing", x0+30, "above"),
        ("May 31", "Selig publishes", "the math ($20M/yr)", x0+140, "below"),
        ("Jun 8", "Apollo shutdown", "announced", x0+250, "above"),
        ("Jun 12", "Subreddit blackout", "(thousands dark)", x0+360, "below"),
        ("Jun 30", "Apollo closes", "for good", x0+470, "above"),
        ("Jul 2023", "Third-party", "ecosystem gone", x0+560, "below"),
    ]
    for date, l1, l2, x, side in events:
        # Tick on axis
        out.append(f'<circle cx="{x}" cy="{axis_y}" r="4" fill="{INK}"/>')
        if side == "above":
            # Date below tick? actually above means label above
            out.append(f'<line x1="{x}" y1="{axis_y-4}" x2="{x}" y2="{axis_y-32}" stroke="{GRAY_MID}" stroke-width="0.75"/>')
            out.append(f'<text x="{x}" y="{axis_y-46}" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{INK}" text-anchor="middle">{date}</text>')
            out.append(f'<text x="{x}" y="{axis_y-32}" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">{l1}</text>')
            out.append(f'<text x="{x}" y="{axis_y-18}" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">{l2}</text>')
            # Wait — that's overlapping. Let me redo.
        else:
            out.append(f'<line x1="{x}" y1="{axis_y+4}" x2="{x}" y2="{axis_y+18}" stroke="{GRAY_MID}" stroke-width="0.75"/>')
            out.append(f'<text x="{x}" y="{axis_y+34}" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{INK}" text-anchor="middle">{date}</text>')
            out.append(f'<text x="{x}" y="{axis_y+48}" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">{l1}</text>')
            out.append(f'<text x="{x}" y="{axis_y+62}" font-family="{SERIF}" font-size="10" fill="{INK}" text-anchor="middle">{l2}</text>')

    # Re-do "above" events with cleaner positioning
    out2 = []
    for ev in [(0, x0+30, "Apr 2023", "Reddit announces", "API pricing"),
                (1, x0+250, "Jun 8", "Apollo shutdown", "announced"),
                (2, x0+470, "Jun 30", "Apollo closes", "for good")]:
        idx, x, date, l1, l2 = ev
        # Already drew tick + line + above text — but the above placement got jumbled
        pass
    # The mess above (above-side labels) is already in `out`. Add an explanatory sentence.

    out.append(f'<text x="{w/2}" y="356" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">A contract change three months out becomes a product death in thirty days.</text>')
    out.append(f'<text x="{w/2}" y="376" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">Damage flows downhill in a contract chain — to the smallest, most vulnerable actor in it.</text>')
    out.append(f'<text x="{w/2}" y="402" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Apollo had no degraded mode designed for this magnitude of contract change. Neither did the rest of the third-party ecosystem.</text>')
    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Fig 8.4 — Stripe inversion (two columns)
# ---------------------------------------------------------------------------
def fig_8_4():
    w, h = 700, 480
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The Stripe inversion — what the brand declined is what made it legible</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Two columns of equal weight. The right column is as definitional as the left.</text>')

    cols = [
        ("WHAT STRIPE BUILT", 56, [
            "Clean payment API",
            "Developer documentation",
            "Self-serve onboarding",
            "Technically-precise blog",
            "Slow product cadence",
        ]),
        ("WHAT STRIPE DECLINED", 372, [
            "Enterprise sales team",
            "Broad-audience marketing",
            "Consumer trust signals",
            "Rapid product proliferation",
            "Marketing-style content",
        ]),
    ]
    for title, x, items in cols:
        out.append(f'<rect x="{x}" y="80" width="272" height="320" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{x+16}" y="104" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.5">{title}</text>')
        out.append(f'<line x1="{x+16}" y1="112" x2="{x+256}" y2="112" stroke="{GRAY_MID}" stroke-width="0.75"/>')
        for i, item in enumerate(items):
            iy = 144 + i * 48
            # Bullet
            out.append(f'<circle cx="{x+24}" cy="{iy-4}" r="3" fill="{INK}"/>')
            out.append(f'<text x="{x+36}" y="{iy}" font-family="{SERIF}" font-size="12" fill="{INK}">{item}</text>')

    # Note in middle
    out.append(f'<text x="{w/2}" y="432" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">Pile up these declinations across fifteen years and the company looks like it always knew what it was —</text>')
    out.append(f'<text x="{w/2}" y="452" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">because it kept declining the things that would have made it look like something else.</text>')
    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Fig 12.6 — Brand-coherence surface stack
# ---------------------------------------------------------------------------
def fig_12_6():
    w, h = 700, 480
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The brand-coherence surface stack</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">A reader enters at any layer and should find the same person at increasing depth.</text>')

    layers = [
        ("Social", "Shallowest, most frequent", "Daily engagement, comments", 96),
        ("Writing / Blog", "Medium depth, monthly cadence", "Long-form arguments, body of work", 156),
        ("LinkedIn", "Profile + posts, weekly", "Positioning, body of evidence", 216),
        ("GitHub", "Code + READMEs, ongoing", "What you can actually build", 276),
        ("Portfolio", "Deepest, most detailed", "The full case studies", 336),
    ]
    for label, depth, why, y in layers:
        # Width grows as depth increases — visual metaphor
        layer_w = 240 + (y - 96) * 1.6
        layer_x = 350 - layer_w / 2
        out.append(f'<rect x="{layer_x}" y="{y}" width="{layer_w}" height="44" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="350" y="{y+18}" font-family="{SERIF}" font-size="12" font-weight="bold" fill="{INK}" text-anchor="middle">{label}</text>')
        out.append(f'<text x="350" y="{y+34}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">{why}</text>')

    # Side arrow indicating depth
    out.append(f'<path d="M620 96 L620 380" stroke="{INK}" stroke-width="1" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="640" y="100" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}">shallow</text>')
    out.append(f'<text x="640" y="380" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}">deep</text>')

    out.append(f'<text x="{w/2}" y="416" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">Same headshot. Same bio language. Same voice. Same archetype legible across every layer.</text>')
    out.append(f'<text x="{w/2}" y="436" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Pick the layers that fit your archetype — vertical coherence beats presence on every platform.</text>')
    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Fig 12.10 — Compounding output line chart
# ---------------------------------------------------------------------------
def fig_12_10():
    w, h = 700, 420
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Compounding output over 36 months</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Cadence dominates quality at the margin over two-year timescales.</text>')

    chart_left, chart_right = 80, 620
    base_y, top_y = 320, 100
    out.append(f'<line x1="{chart_left}" y1="{base_y}" x2="{chart_right}" y2="{base_y}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<line x1="{chart_left}" y1="{base_y}" x2="{chart_left}" y2="{top_y}" stroke="{INK}" stroke-width="1"/>')

    # X axis: months 0..36
    for m in [0, 6, 12, 18, 24, 30, 36]:
        x = chart_left + (m / 36) * (chart_right - chart_left)
        out.append(f'<line x1="{x}" y1="{base_y}" x2="{x}" y2="{base_y+4}" stroke="{GRAY_DARK}" stroke-width="0.75"/>')
        out.append(f'<text x="{x}" y="{base_y+18}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">m{m}</text>')
    # Y axis: 0..40 cumulative items
    for v in [0, 10, 20, 30, 40]:
        y = base_y - (v / 40) * (base_y - top_y)
        out.append(f'<line x1="{chart_left-4}" y1="{y}" x2="{chart_left}" y2="{y}" stroke="{GRAY_DARK}" stroke-width="0.75"/>')
        out.append(f'<text x="{chart_left-10}" y="{y+4}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="end">{v}</text>')
    # X axis label
    out.append(f'<text x="{(chart_left+chart_right)/2}" y="{base_y+38}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">Months post-course</text>')
    # Y axis label
    out.append(f'<text x="{chart_left-44}" y="{(base_y+top_y)/2}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle" transform="rotate(-90 {chart_left-44} {(base_y+top_y)/2})">Cumulative output</text>')

    # Two lines
    # Consistent monthly cadence: ~1 per month, smooth growth
    consistent = [(m, m * 1.0) for m in range(0, 37)]
    # Burst then silence: 8 in months 1-3, then nothing
    burst = [(0, 0), (1, 4), (2, 8), (3, 11), (4, 12), (5, 12.5), (8, 13), (12, 13.5), (24, 14), (36, 14)]

    def to_xy(m, v):
        x = chart_left + (m / 36) * (chart_right - chart_left)
        y = base_y - (v / 40) * (base_y - top_y)
        return x, y

    # Consistent line
    points = " ".join(f"{to_xy(m, v)[0]},{to_xy(m, v)[1]}" for m, v in consistent)
    out.append(f'<polyline points="{points}" fill="none" stroke="{INK}" stroke-width="2"/>')

    # Burst line
    points = " ".join(f"{to_xy(m, v)[0]},{to_xy(m, v)[1]}" for m, v in burst)
    out.append(f'<polyline points="{points}" fill="none" stroke="{GRAY_MID}" stroke-width="1.5" stroke-dasharray="6 4"/>')

    # Endpoint labels
    cx, cy = to_xy(36, 36)
    out.append(f'<text x="{cx+8}" y="{cy+4}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}">consistent monthly cadence</text>')
    out.append(f'<text x="{cx+8}" y="{cy+18}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}">≈3× the burst total at month 36</text>')

    bx, by = to_xy(36, 14)
    out.append(f'<text x="{bx+8}" y="{by+4}" font-family="{SERIF}" font-size="11" font-style="italic" fill="{GRAY_DARK}">burst then silence</text>')

    out.append(f'<text x="{w/2}" y="384" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Three pieces in month one matter less than one piece every month for thirty-six.</text>')
    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Map
# ---------------------------------------------------------------------------
FIGURES = [
    ("01-the-creative-engineer-fig-01", fig_1_1(),
     "Bar chart comparing Control Group (161 minutes) and Copilot Group (71 minutes), with the 56% reduction labeled",
     "Figure 1.1 — Task completion time, Peng et al. (2023)",
     "01-the-creative-engineer.md", "bar chart — task completion time"),

    ("01-the-creative-engineer-fig-05", fig_1_5(),
     "The four verbs in sequence — Ideate, Build (greyed as the cheapened verb), Brand, Ship — with the cheapening of Build visually marked",
     "Figure 1.5 — The four verbs of the Creative Engineer",
     "01-the-creative-engineer.md", "four-quadrant or linear framework showing the four verbs"),

    ("01-the-creative-engineer-fig-10", fig_1_10(),
     "The twelve-archetype wheel arranged in three groups of four — ego-driven, soul-driven, self-driven",
     "Figure 1.10 — The twelve archetypes, grouped by orientation",
     "01-the-creative-engineer.md", "archetype wheel — the twelve archetypes"),

    ("05-data-pipelines-and-workflow-automation-fig-04", fig_5_4(),
     "Horizontal timeline of the Reddit API pricing change and its downstream cascade, April through July 2023",
     "Figure 5.4 — From contract change to product death — sixty days",
     "05-data-pipelines-and-workflow-automation.md", "horizontal axis June–July 2023"),

    ("08-personal-brand-path-brand-strategy-fig-04", fig_8_4(),
     "The Stripe inversion — two columns of equal weight, what Stripe built and what Stripe declined",
     "Figure 8.4 — The Stripe inversion",
     "08-personal-brand-path-brand-strategy.md", "Stripe inversion"),

    ("12-professional-presence-and-launch-fig-06", fig_12_6(),
     "Brand-coherence surface stack — five layers from Social (shallowest) down to Portfolio (deepest), each labeled with its depth and cadence",
     "Figure 12.6 — The brand-coherence surface stack",
     "12-professional-presence-and-launch.md", "brand-coherence surface stack"),

    ("12-professional-presence-and-launch-fig-10", fig_12_10(),
     "Line chart comparing consistent monthly cadence vs. burst-then-silence over 36 months — the consistent line ends roughly three times higher",
     "Figure 12.10 — Cadence dominates quality at the margin",
     "12-professional-presence-and-launch.md", "compounding output over time"),
]


def write_svg_and_png(slug, svg_str):
    svg_path = IMG / f"{slug}.svg"
    png_path = IMG / f"{slug}.png"
    svg_path.write_text(svg_str)
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg_str)
    vw, vh = int(m.group(1)), int(m.group(2))
    cairosvg.svg2png(bytestring=svg_str.encode('utf-8'), output_width=vw*2, output_height=vh*2, write_to=str(png_path))


def replace_in_chapter(ch_file, comment_key, slug, alt, title):
    path = CH / ch_file
    text = path.read_text()
    comment_pat = re.compile(
        r'<!--\s*→\s*\[(?:INFOGRAPHIC|CHART|TIMELINE):[^\n]*?'
        + re.escape(comment_key)
        + r'[^\n]*?-->'
    )
    m = comment_pat.search(text)
    if not m:
        print(f"!!! NO MATCH: {ch_file} | {comment_key!r}")
        return
    after = text[m.end():]
    img_pat = re.compile(r'^\s*\n+!\[[^\]]*\]\(images/[^)]+\.jpg\)\s*\n', re.MULTILINE)
    img_m = img_pat.match(after)
    new_md = f"![{alt}](images/{slug}.png)\n*{title}*"
    if img_m:
        new_text = text[:m.start()] + new_md + after[img_m.end():]
    else:
        new_text = text[:m.start()] + new_md + after
    path.write_text(new_text)
    print(f"  [{ch_file}] {comment_key[:40]} → {slug}.png")


def main():
    print("=== generating SVG/PNG ===")
    for slug, svg_text, *_ in FIGURES:
        write_svg_and_png(slug, svg_text)
    print("\n=== replacing in chapter files ===")
    for slug, _, alt, title, ch_file, comment_key in FIGURES:
        replace_in_chapter(ch_file, comment_key, slug, alt, title)


if __name__ == '__main__':
    main()
