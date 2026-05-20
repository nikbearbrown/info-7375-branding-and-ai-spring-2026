#!/usr/bin/env python3
"""Pass 2 — generate 14 SVG+PNG figures for branding-and-ai chapters and replace
the FIGURE/IMAGE/DIAGRAM comments + adjacent .jpg placeholders with .png refs.
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
# Chapter 01
# ---------------------------------------------------------------------------

def fig_1_3():
    """Separating vs Pooling Equilibrium — two-column schematic."""
    w, h = 700, 420
    out = svg_open(w, h)
    # Title
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Separating vs. Pooling Equilibrium</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">A signal works only when its cost differs by type. When tooling makes the signal cheap for everyone, separation collapses into pooling.</text>')

    # Two columns
    cols = [
        ("SEPARATING EQUILIBRIUM", 56, [
            ("High-productivity candidate", "Signal cost: low (relative to ability)", "Sends the signal"),
            ("Low-productivity candidate", "Signal cost: high (relative to ability)", "Cannot afford the signal"),
            ("Employer", "Observes the signal — and learns who is who", ""),
        ], "The signal sorts. Hiring works."),
        ("POOLING EQUILIBRIUM", 372, [
            ("High-productivity candidate", "Signal cost: low", "Sends the signal"),
            ("Low-productivity candidate", "Signal cost: low (AI tooling)", "Also sends the signal"),
            ("Employer", "Observes the signal — and learns nothing", ""),
        ], "The signal pools. Hiring stops working from this signal."),
    ]
    for title, x, rows, footer in cols:
        out.append(f'<rect x="{x}" y="80" width="272" height="280" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{x+16}" y="100" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.5">{title}</text>')
        out.append(f'<line x1="{x+16}" y1="108" x2="{x+256}" y2="108" stroke="{GRAY_MID}" stroke-width="0.75"/>')
        for i, (head, line2, line3) in enumerate(rows):
            ry = 124 + i*72
            out.append(f'<text x="{x+16}" y="{ry}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}">{head}</text>')
            out.append(f'<text x="{x+16}" y="{ry+16}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}">{line2}</text>')
            if line3:
                out.append(f'<text x="{x+16}" y="{ry+32}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}">{line3}</text>')
        out.append(f'<text x="{x+136}" y="346" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">{footer}</text>')

    # Bottom note
    out.append(f'<text x="{w/2}" y="394" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">When the cost-structure of a signal collapses, the signal collapses with it. The fix is not a louder signal — it is a different signal.</text>')
    out.append('</svg>')
    return "\n".join(out)


def fig_1_8():
    """Anthropic vs OpenAI homepage — side-by-side mockup."""
    w, h = 700, 420
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Anthropic / OpenAI — same capability, different positioning</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Two homepage hero sections, two audiences claimed. Brand is the choice that the technology cannot make for you.</text>')

    cols = [
        ("anthropic.com", 56, "Sage register — patient, evidence-led", [
            "AI safety, alignment research,",
            "and large-scale models built",
            "for the long term.",
            "",
            "[ Read the research ]",
        ], "Audience: researchers, infra teams, long-horizon buyers."),
        ("openai.com", 372, "Hero / Magician register — capability foregrounded", [
            "Powerful AI for everyone.",
            "Build, ship, integrate —",
            "in minutes, not months.",
            "",
            "[ Try it now ]",
        ], "Audience: developers, consumers, fast-iteration buyers."),
    ]
    for url, x, lab, lines, footer in cols:
        out.append(f'<rect x="{x}" y="80" width="272" height="280" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        # url bar
        out.append(f'<rect x="{x+16}" y="96" width="240" height="22" fill="{WHITE}" stroke="{GRAY_MID}" stroke-width="0.75"/>')
        out.append(f'<text x="{x+24}" y="111" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}">{url}</text>')
        # label
        out.append(f'<text x="{x+16}" y="138" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1">{lab}</text>')
        # hero text
        for i, line in enumerate(lines):
            out.append(f'<text x="{x+16}" y="{162+i*22}" font-family="{SERIF}" font-size="13" fill="{INK}">{line}</text>')
        # footer
        out.append(f'<line x1="{x+16}" y1="332" x2="{x+256}" y2="332" stroke="{GRAY_LIGHT}" stroke-width="0.75" stroke-dasharray="4 3"/>')
        out.append(f'<text x="{x+136}" y="350" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">{footer}</text>')

    out.append('</svg>')
    return "\n".join(out)


def fig_1_12():
    """Two GitHub profile pages — Engineer A vs Engineer B."""
    w, h = 700, 480
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Two GitHub profiles, two archetypes legible at a glance</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The README, the project list, the negative space — all signal who the engineer is for.</text>')

    cols = [
        ("ENGINEER A — Sage shadow / Critic", 56, [
            ("Bio:", "Senior eng. Strong opinions, lightly held."),
            ("Pinned repos:", "fork-of-mit-license · my-dotfiles · old-side-project"),
            ("READMEs:", "Sparse. Code-only. Tone: critical."),
            ("Activity:", "Issue threads with sharp corrections"),
            ("Negative space:", "No tutorials. No accessibility framing."),
        ], "Reads as: the colleague you don't ask twice."),
        ("ENGINEER B — Sage / Teacher", 372, [
            ("Bio:", "Builds tools that make hard things teachable."),
            ("Pinned repos:", "rss-pipeline · llm-eval-kit · accessibility-ux-toolkit"),
            ("READMEs:", "Tutorial-style. Voice: warm, precise."),
            ("Activity:", "Writes guides, answers questions"),
            ("Negative space:", "No drive-by comments. No flame wars."),
        ], "Reads as: the colleague you bring questions to."),
    ]
    for title, x, rows, footer in cols:
        out.append(f'<rect x="{x}" y="80" width="272" height="340" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{x+16}" y="100" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.2">{title}</text>')
        out.append(f'<line x1="{x+16}" y1="108" x2="{x+256}" y2="108" stroke="{GRAY_MID}" stroke-width="0.75"/>')
        for i, (lab, val) in enumerate(rows):
            ry = 132 + i*44
            out.append(f'<text x="{x+16}" y="{ry}" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{GRAY_DARK}">{lab}</text>')
            out.append(f'<text x="{x+16}" y="{ry+16}" font-family="{SERIF}" font-size="11" fill="{INK}">{val}</text>')
        out.append(f'<line x1="{x+16}" y1="380" x2="{x+256}" y2="380" stroke="{GRAY_LIGHT}" stroke-width="0.75" stroke-dasharray="4 3"/>')
        out.append(f'<text x="{x+136}" y="402" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">{footer}</text>')

    out.append('</svg>')
    return "\n".join(out)


def fig_1_13():
    """Three-level stack — Spence / Four-Verb / Archetype."""
    w, h = 700, 420
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Three frames, one argument</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Each layer is built on the one below; remove any layer and the others lose their grip.</text>')

    layers = [
        ("ARCHETYPE SYSTEM", "explains *how* to execute Brand", 96, "The role you play in your audience's story"),
        ("FOUR-VERB FRAMEWORK", "explains *what* the portfolio must demonstrate", 196, "Ideate · Build · Brand · Ship"),
        ("SPENCE MECHANISM", "explains *why* brand matters", 296, "When build cheapens, separation moves to upstream and downstream verbs"),
    ]
    for label, why, y, desc in layers:
        out.append(f'<rect x="120" y="{y}" width="460" height="76" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="350" y="{y+22}" font-family="{SERIF}" font-size="12" font-weight="bold" fill="{INK}" text-anchor="middle">{label}</text>')
        out.append(f'<text x="350" y="{y+40}" font-family="{SERIF}" font-size="11" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">{why}</text>')
        out.append(f'<text x="350" y="{y+62}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">{desc}</text>')
    # Upward arrows between layers
    for y in [288, 188]:
        out.append(f'<path d="M350 {y+8} L350 {y-12}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')

    out.append(f'<text x="{w/2}" y="396" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Why → What → How. The student who reads the levels in this order builds an integrated practice.</text>')
    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Chapter 05
# ---------------------------------------------------------------------------

def fig_5_1():
    """Five-node pipeline, one contract failing, downstream degrades."""
    w, h = 700, 420
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">A pipeline is a chain of contracts</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Each arrow is a contract owned by someone else. The pipeline runs as long as every contract holds.</text>')

    nodes = [
        ("Trigger", 64),
        ("Ingest", 192),
        ("Transform", 320),
        ("LLM step", 448),
        ("Output", 576),
    ]
    cy = 200
    for name, cx in nodes:
        out.append(f'<rect x="{cx-44}" y="{cy-26}" width="88" height="52" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{cx}" y="{cy+5}" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">{name}</text>')
    # Arrows between nodes — 4 contracts
    contracts = [
        ("contract", 108, 148, ""),
        ("contract", 236, 276, "?"),  # the failure point
        ("contract", 364, 404, ""),
        ("contract", 492, 532, ""),
    ]
    for label, x1, x2, marker in contracts:
        # Arrow
        if marker == "?":
            # Highlight failure: thicker stroke and a question mark
            out.append(f'<path d="M{x1} {cy} L{x2} {cy}" stroke="{INK}" stroke-width="2" fill="none" marker-end="url(#arrow)" stroke-dasharray="4 3"/>')
            out.append(f'<text x="{(x1+x2)/2}" y="{cy-12}" font-family="{SERIF}" font-size="14" font-weight="bold" fill="{INK}" text-anchor="middle">?</text>')
            out.append(f'<text x="{(x1+x2)/2}" y="{cy+22}" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">contract failure</text>')
        else:
            out.append(f'<path d="M{x1} {cy} L{x2} {cy}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
            out.append(f'<text x="{(x1+x2)/2}" y="{cy-8}" font-family="{SERIF}" font-size="9" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">{label}</text>')

    # Downstream node degraded
    cx_last = 576
    out.append(f'<text x="{cx_last}" y="{cy+50}" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">degraded</text>')
    out.append(f'<text x="{cx_last}" y="{cy+64}" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">output</text>')

    out.append(f'<text x="{w/2}" y="320" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">The pipeline does not crash. It runs, in a degraded mode, because Ingest&#8217;s contract failure was anticipated.</text>')
    out.append(f'<text x="{w/2}" y="340" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">The brand consequence — the user-facing failure — is contained to the affected step.</text>')
    out.append(f'<text x="{w/2}" y="380" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">A pipeline is not a piece of code. It is a chain of contracts, each subject to change without your consent.</text>')
    out.append('</svg>')
    return "\n".join(out)


def fig_5_7():
    """Side-by-side: Python script vs n8n graph."""
    w, h = 700, 480
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Two pipeline implementations — same dependencies, different visibility</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">In code, contracts are buried in the file. In a workflow graph, contracts are nodes you can see, document, and swap.</text>')

    # LEFT: python script
    lx = 56
    out.append(f'<rect x="{lx}" y="80" width="272" height="340" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="{lx+16}" y="100" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.2">PYTHON SCRIPT</text>')
    out.append(f'<line x1="{lx+16}" y1="108" x2="{lx+256}" y2="108" stroke="{GRAY_MID}" stroke-width="0.75"/>')
    code = [
        "def run():",
        "    raw = requests.get(REDDIT_URL)",
        "    items = parse(raw.text)",
        "    seen = load_seen_urls()",
        "    items = dedup(items, seen)",
        "    scored = call_openai(items)",
        "    write_to_sheet(scored)",
        "    write_log(len(scored))",
    ]
    for i, line in enumerate(code):
        out.append(f'<text x="{lx+16}" y="{132+i*22}" font-family="Courier New, monospace" font-size="10" fill="{INK}">{line}</text>')
    out.append(f'<line x1="{lx+16}" y1="318" x2="{lx+256}" y2="318" stroke="{GRAY_LIGHT}" stroke-width="0.75" stroke-dasharray="4 3"/>')
    out.append(f'<text x="{lx+136}" y="346" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Dependencies interwoven.</text>')
    out.append(f'<text x="{lx+136}" y="362" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Contracts unlabeled.</text>')
    out.append(f'<text x="{lx+136}" y="392" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">Swap one API → touch the file.</text>')

    # RIGHT: n8n graph
    rx = 372
    out.append(f'<rect x="{rx}" y="80" width="272" height="340" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="{rx+16}" y="100" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.2">n8n WORKFLOW</text>')
    out.append(f'<line x1="{rx+16}" y1="108" x2="{rx+256}" y2="108" stroke="{GRAY_MID}" stroke-width="0.75"/>')
    nodes = [
        ("Schedule", 132),
        ("HTTP: Reddit", 172),
        ("Code: dedup", 212),
        ("OpenAI score", 252),
        ("Sheets: write", 292),
    ]
    for name, y in nodes:
        out.append(f'<rect x="{rx+72}" y="{y-14}" width="160" height="28" fill="{WHITE}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{rx+152}" y="{y+5}" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">{name}</text>')
    # Vertical connectors
    for y in [132, 172, 212, 252]:
        out.append(f'<path d="M{rx+152} {y+14} L{rx+152} {y+26}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')

    # Callout
    out.append(f'<path d="M{rx+232} {172} L{rx+260} {172}" stroke="{INK}" stroke-width="1" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="{rx+8}" y="362" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}">Each contract = one node.</text>')
    out.append(f'<text x="{rx+8}" y="378" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}">Swap a node without touching the rest.</text>')
    out.append(f'<text x="{rx+136}" y="402" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">Discipline becomes structural.</text>')

    out.append(f'<text x="{w/2}" y="450" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">A Python pipeline can achieve the same result with sufficient discipline. n8n makes the discipline structural rather than optional.</text>')
    out.append('</svg>')
    return "\n".join(out)


def fig_5_8():
    """n8n node editor interface — annotated mockup."""
    w, h = 700, 480
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The n8n node editor — anatomy of a workflow surface</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Four things to recognize before you install: the node panel, a node, a connection, and the description field.</text>')

    # Outer frame (n8n window)
    out.append(f'<rect x="56" y="80" width="588" height="320" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')

    # Left node panel
    out.append(f'<rect x="72" y="96" width="120" height="288" fill="{WHITE}" stroke="{GRAY_MID}" stroke-width="0.75"/>')
    out.append(f'<text x="80" y="114" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{GRAY_DARK}">NODES</text>')
    panel_items = ["HTTP Request", "Code", "Schedule", "OpenAI", "Google Sheets", "Webhook", "If / Switch", "Set"]
    for i, item in enumerate(panel_items):
        out.append(f'<text x="80" y="{136+i*24}" font-family="{SERIF}" font-size="10" fill="{INK}">{item}</text>')

    # Canvas with two nodes
    nx1, ny1 = 248, 188
    nx2, ny2 = 432, 188
    for nx, ny, name, sub in [(nx1, ny1, "HTTP Request", "GET RSS feed"),
                                (nx2, ny2, "Code", "Transform")]:
        out.append(f'<rect x="{nx}" y="{ny}" width="116" height="56" fill="{WHITE}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{nx+58}" y="{ny+22}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">{name}</text>')
        out.append(f'<text x="{nx+58}" y="{ny+40}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">{sub}</text>')
        # ports
        out.append(f'<circle cx="{nx}" cy="{ny+28}" r="3" fill="{INK}"/>')
        out.append(f'<circle cx="{nx+116}" cy="{ny+28}" r="3" fill="{INK}"/>')
    # Connection
    out.append(f'<path d="M{nx1+116} {ny1+28} L{nx2} {ny2+28}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')

    # Description field below
    out.append(f'<rect x="248" y="280" width="300" height="100" fill="{WHITE}" stroke="{GRAY_MID}" stroke-width="0.75"/>')
    out.append(f'<text x="256" y="298" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{GRAY_DARK}">NODE DESCRIPTION</text>')
    desc = [
        "Hacker News RSS — no auth required.",
        "No documented rate limit. Stable Atom",
        "format since 2006. Risk: low.",
    ]
    for i, line in enumerate(desc):
        out.append(f'<text x="256" y="{318+i*16}" font-family="{SERIF}" font-size="10" fill="{INK}">{line}</text>')

    # Callouts (numbered)
    callouts = [
        ("(1) Node panel", 72+60, 96, 12, -8, "left"),
        ("(2) Node + I/O ports", nx1+58, ny1, -50, -28, "right"),
        ("(3) Connection — data flows here", (nx1+nx2)/2+58, ny1+28, 0, -56, "right"),
        ("(4) Description — document the contract", 248+150, 280, 0, 110, "right"),
    ]
    # Number the callouts on the canvas with simple text labels offset
    out.append(f'<text x="78" y="92" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{INK}">(1)</text>')
    out.append(f'<text x="{nx1-12}" y="{ny1-4}" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{INK}">(2)</text>')
    out.append(f'<text x="{(nx1+nx2)/2+58}" y="{ny1+22}" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{INK}" text-anchor="middle">(3)</text>')
    out.append(f'<text x="{248-12}" y="{300}" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{INK}">(4)</text>')

    # Legend
    legend = [
        "(1) Node panel — available node types",
        "(2) Node on canvas — labeled input / output ports",
        "(3) Connection — data flows here",
        "(4) Description field — where contracts are documented",
    ]
    for i, line in enumerate(legend):
        out.append(f'<text x="60" y="{420+i*14}" font-family="{SERIF}" font-size="10" fill="{INK}">{line}</text>')

    out.append('</svg>')
    return "\n".join(out)


def fig_5_9():
    """Madison Intelligence Agent workflow graph."""
    w, h = 700, 480
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Madison Intelligence Agent — production-grade workflow architecture</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Each design choice is a response to a specific failure mode — not a stylistic preference.</text>')

    # Trigger
    out.append(f'<rect x="64" y="100" width="120" height="40" fill="{WHITE}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="124" y="117" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">Schedule</text>')
    out.append(f'<text x="124" y="131" font-family="{SERIF}" font-size="9" fill="{GRAY_DARK}" text-anchor="middle">every 6 hours</text>')

    # Parallel ingestion (3 branches)
    branches = [("RSS feeds", 100), ("Google News", 200), ("Reddit API", 300)]
    for name, by in branches:
        out.append(f'<rect x="248" y="{by-20}" width="120" height="40" fill="{WHITE}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="308" y="{by-2}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">HTTP: {name}</text>')
        # Arrow from trigger to branch
        out.append(f'<path d="M184 120 L248 {by}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')

    # Deduplication
    dx, dy = 408, 200
    out.append(f'<rect x="{dx}" y="{dy-20}" width="120" height="40" fill="{WHITE}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="{dx+60}" y="{dy-2}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">Code: dedup</text>')
    out.append(f'<text x="{dx+60}" y="{dy+12}" font-family="{SERIF}" font-size="9" fill="{GRAY_DARK}" text-anchor="middle">seen-URL store</text>')
    # Branches converge
    for name, by in branches:
        out.append(f'<path d="M368 {by} L{dx} {dy}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')

    # LLM scoring
    lx, ly = 568, 200
    out.append(f'<rect x="{lx}" y="{ly-20}" width="100" height="40" fill="{WHITE}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="{lx+50}" y="{ly-2}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">OpenAI</text>')
    out.append(f'<text x="{lx+50}" y="{ly+12}" font-family="{SERIF}" font-size="9" fill="{GRAY_DARK}" text-anchor="middle">score + summarize</text>')
    out.append(f'<path d="M528 {dy} L{lx} {ly}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')

    # Output (two endpoints)
    out.append(f'<rect x="{lx-50}" y="320" width="120" height="40" fill="{WHITE}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="{lx+10}" y="338" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">Sheets: append</text>')
    out.append(f'<text x="{lx+10}" y="352" font-family="{SERIF}" font-size="9" fill="{GRAY_DARK}" text-anchor="middle">scored items</text>')
    out.append(f'<rect x="248" y="320" width="120" height="40" fill="{WHITE}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="308" y="338" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">Sheets: run log</text>')
    out.append(f'<text x="308" y="352" font-family="{SERIF}" font-size="9" fill="{GRAY_DARK}" text-anchor="middle">timestamp + count</text>')
    out.append(f'<path d="M{lx+50} {ly+20} L{lx+10} 320" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<path d="M{dx+60} {dy+20} L308 320" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')

    # Callouts
    callouts = [
        "(1) Parallel ingestion — single source down ≠ pipeline stalls",
        "(2) Seen-URL store — no double-scoring across runs",
        "(3) LLM scoring — inference as a step inside the workflow",
        "(4) Run log — visibility independent of execution health",
    ]
    for i, line in enumerate(callouts):
        out.append(f'<text x="60" y="{406+i*16}" font-family="{SERIF}" font-size="10" fill="{INK}">{line}</text>')

    out.append('</svg>')
    return "\n".join(out)


def fig_5_11():
    """Three-level stack — pipeline disciplines."""
    w, h = 700, 420
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Three pipeline disciplines, one brand outcome</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Parallel structure to the Spence / Four-Verb / Archetype stack — each layer rests on the one below.</text>')

    layers = [
        ("CONTRACT MONITORING", "*how* to know before users do", 96, "Status-page feeds, billing alerts, error workflows"),
        ("DEGRADED MODE DESIGN", "*what* to do when a contract fails", 196, "Informative failure → partial degradation → fallback → graceful staleness"),
        ("CONTRACT DOCUMENTATION", "*why* it matters", 296, "Every external dependency named; *subject to change* explicitly acknowledged"),
    ]
    for label, why, y, desc in layers:
        out.append(f'<rect x="120" y="{y}" width="460" height="76" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="350" y="{y+22}" font-family="{SERIF}" font-size="12" font-weight="bold" fill="{INK}" text-anchor="middle">{label}</text>')
        out.append(f'<text x="350" y="{y+40}" font-family="{SERIF}" font-size="11" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">{why}</text>')
        out.append(f'<text x="350" y="{y+62}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">{desc}</text>')
    for y in [288, 188]:
        out.append(f'<path d="M350 {y+8} L350 {y-12}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')

    out.append(f'<text x="{w/2}" y="396" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">A pipeline failure is a brand failure. The brand that pays is the one whose name is on the front page.</text>')
    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Chapter 08-personal
# ---------------------------------------------------------------------------

def fig_8_2():
    """Seven brand components dependency chain."""
    w, h = 700, 600
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The seven components, in the order they constrain each other</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">A contradiction anywhere upstream propagates down. Negative space is downstream of everything.</text>')

    layers = [
        ("MISSION", "What the company exists to do", 84),
        ("VISION", "The world if you succeed", 152),
        ("VALUES", "What the company won't compromise", 220),
        ("UVP", "What you offer that competitors don't", 288),
        ("ARCHETYPE", "The role you play in the audience's story", 356),
        ("VOICE", "How the company speaks", 424),
        ("POSITIONING", "Where you sit relative to the actual alternative", 484),
    ]
    for label, sub, y in layers[:-1]:
        out.append(f'<rect x="160" y="{y}" width="380" height="48" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="350" y="{y+18}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">{label}</text>')
        out.append(f'<text x="350" y="{y+36}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">{sub}</text>')
    # Positioning layer
    label, sub, y = layers[-1]
    out.append(f'<rect x="160" y="{y}" width="380" height="48" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="350" y="{y+18}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">{label}</text>')
    out.append(f'<text x="350" y="{y+36}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">{sub}</text>')

    # Downward arrows between consecutive layers
    for i in range(len(layers)-1):
        y1 = layers[i][2] + 48
        y2 = layers[i+1][2]
        out.append(f'<path d="M350 {y1} L350 {y2-2}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')

    # Negative space at the bottom — downstream of all
    ny = 552
    out.append(f'<rect x="80" y="{ny}" width="540" height="40" fill="{INK}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="350" y="{ny+24}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">NEGATIVE SPACE — downstream of all seven; what the company refuses to do</text>')
    # Connect from positioning to negative space with multiple arrows from above
    for x in [220, 350, 480]:
        out.append(f'<path d="M{x} 532 L{x} {ny-2}" stroke="{INK}" stroke-width="1" stroke-dasharray="4 3" fill="none"/>')

    out.append('</svg>')
    return "\n".join(out)


def fig_8_8():
    """Circular consistency check — seven components in a circle."""
    w, h = 700, 600
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The internal consistency check — every adjacent pair must hold</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">If any arrow has a contradiction, the circle breaks. The strategy document is a hypothesis; coherence makes it usable.</text>')

    import math
    cx, cy, r = 350, 320, 180
    components = ["Mission", "Vision", "Values", "UVP", "Archetype", "Voice", "Positioning"]
    n = len(components)
    positions = []
    for i, comp in enumerate(components):
        angle = -math.pi/2 + (2*math.pi * i / n)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        positions.append((x, y, comp))
        # Box
        out.append(f'<rect x="{x-52}" y="{y-16}" width="104" height="32" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{x}" y="{y+5}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">{comp}</text>')

    # Arc connectors with labels
    questions = [
        "Does the vision realize the mission?",
        "Do the values reach the vision?",
        "Does the UVP express the values?",
        "Does the archetype anchor the UVP?",
        "Does the voice fit the archetype?",
        "Does positioning make UVP legible?",
        "Do values express archetype core drive?",
    ]
    for i in range(n):
        x1, y1, _ = positions[i]
        x2, y2, _ = positions[(i+1) % n]
        # Arc using a path with a control point bowed outward from center
        midx, midy = (x1+x2)/2, (y1+y2)/2
        # Direction from center to midpoint
        dx, dy = midx - cx, midy - cy
        norm = math.hypot(dx, dy) or 1
        ctrl_x = midx + dx/norm * 20
        ctrl_y = midy + dy/norm * 20
        out.append(f'<path d="M{x1} {y1} Q{ctrl_x} {ctrl_y} {x2} {y2}" stroke="{INK}" stroke-width="1" fill="none" marker-end="url(#arrow)"/>')
        # Question label outside the arc
        label_x = midx + dx/norm * 60
        label_y = midy + dy/norm * 60
        # Truncate label if too long
        q = questions[i]
        if len(q) > 28:
            q = q[:25] + "..."
        out.append(f'<text x="{label_x}" y="{label_y}" font-family="{SERIF}" font-size="9" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">{q}</text>')

    # Center label
    out.append(f'<text x="{cx}" y="{cy-6}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" text-anchor="middle">strategy</text>')
    out.append(f'<text x="{cx}" y="{cy+10}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" text-anchor="middle">document</text>')

    out.append('</svg>')
    return "\n".join(out)


def fig_8_10():
    """Linear flow Ch 4 → Ch 10."""
    w, h = 700, 360
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Where Chapter 8 sits in the four-verb arc</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Chapter 8 is the scaffold — Chapters 9 and 10 take their specificity from it. Vague strategy → vague visual identity → vague story.</text>')

    chs = [
        ("Ch 4", "Career PRD", "Ideate", 56),
        ("Ch 5", "Pipeline", "Build", 160),
        ("Ch 6", "AI layer", "Build", 264),
        ("Ch 7", "Interface", "Build + Ship", 368),
        ("Ch 8", "Brand strategy", "Brand", 472),
        ("Ch 9", "Visual identity", "Brand", 568),
    ]
    cy = 180
    for tag, name, verb, x in chs:
        emph = (tag == "Ch 8")
        fill = INK if emph else CREAM
        text_fill = WHITE if emph else INK
        sub_fill = GRAY_LIGHT if emph else GRAY_DARK
        out.append(f'<rect x="{x-44}" y="{cy-30}" width="88" height="60" fill="{fill}" stroke="{INK}" stroke-width="{2 if emph else 1}"/>')
        out.append(f'<text x="{x}" y="{cy-12}" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{text_fill}" text-anchor="middle">{tag}</text>')
        out.append(f'<text x="{x}" y="{cy+4}" font-family="{SERIF}" font-size="10" fill="{text_fill}" text-anchor="middle">{name}</text>')
        out.append(f'<text x="{x}" y="{cy+22}" font-family="{SERIF}" font-size="9" font-style="italic" fill="{sub_fill}" text-anchor="middle">{verb}</text>')

    # Arrows — increasing width from Ch 8 forward
    for i in range(len(chs)-1):
        x1 = chs[i][3] + 44
        x2 = chs[i+1][3] - 44
        # Make arrows from Ch 8 → Ch 9 thicker
        sw = 2 if chs[i][0] == "Ch 8" else 1.5
        out.append(f'<path d="M{x1} {cy} L{x2} {cy}" stroke="{INK}" stroke-width="{sw}" fill="none" marker-end="url(#arrow)"/>')

    out.append(f'<text x="{w/2}" y="278" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">Brand strategy is the spine. The visual system, the storytelling, and the portfolio narrative</text>')
    out.append(f'<text x="{w/2}" y="296" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">all read off it. The specificity put in here compounds forward.</text>')
    out.append(f'<text x="{w/2}" y="332" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Plus Chapter 10 (Storytelling) — drawing on Mission, Vision, and UVP for the narrative.</text>')
    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Chapter 12
# ---------------------------------------------------------------------------

def fig_12_2():
    """Airbnb argument chain — ten boxes, each implies the next."""
    w, h = 700, 360
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The Airbnb deck — one argument across ten slides</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Each slide implies the next. The audience leaves with one coherent argument, not ten facts.</text>')

    slides = ["Problem", "Solution", "Validation", "Market", "Product", "Model", "Adoption", "Competition", "Team", "Ask"]
    # Two rows of five
    for i, name in enumerate(slides):
        row = i // 5
        col = i % 5
        x = 80 + col * 124
        y = 110 + row * 100
        out.append(f'<rect x="{x}" y="{y}" width="100" height="48" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{x+50}" y="{y+18}" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{GRAY_DARK}" text-anchor="middle">Slide {i+1}</text>')
        out.append(f'<text x="{x+50}" y="{y+36}" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">{name}</text>')

    # Arrows — within row + row break
    for i in range(9):
        if i == 4:  # break to next row
            # arrow from slide 5 down then back to slide 6
            out.append(f'<path d="M630 134 Q670 134 670 220 Q670 234 80 234" stroke="{INK}" stroke-width="1" fill="none" stroke-dasharray="4 3" marker-end="url(#arrow)"/>')
            out.append(f'<text x="640" y="184" font-family="{SERIF}" font-size="9" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">implies</text>')
            continue
        row = i // 5
        col = i % 5
        x1 = 180 + col * 124
        x2 = 80 + (col+1) * 124
        y = 134 + row * 100
        out.append(f'<path d="M{x1} {y} L{x2} {y}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
        # tiny "implies" label every other arrow
        if i % 2 == 0:
            out.append(f'<text x="{(x1+x2)/2}" y="{y-6}" font-family="{SERIF}" font-size="8" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">implies</text>')

    out.append(f'<text x="{w/2}" y="316" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Comprehensive briefing documents do not raise money. Arguments do.</text>')
    out.append('</svg>')
    return "\n".join(out)


def fig_12_11():
    """Four-verb loop — Ideate → Build → Brand → Ship → loop."""
    w, h = 700, 480
    out = svg_open(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The four-verb loop — the practice, not the project</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The course completes one loop. The post-course plan starts the next.</text>')

    import math
    cx, cy, r = 350, 270, 140
    verbs = [
        ("IDEATE", "Ch 4", -math.pi/2),
        ("BUILD", "Ch 5–7", 0),
        ("BRAND", "Ch 8–10", math.pi/2),
        ("SHIP", "Ch 11–12", math.pi),
    ]
    positions = []
    for verb, ch, a in verbs:
        x = cx + r * math.cos(a)
        y = cy + r * math.sin(a)
        positions.append((x, y, verb, ch))
        out.append(f'<rect x="{x-58}" y="{y-26}" width="116" height="52" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{x}" y="{y-4}" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">{verb}</text>')
        out.append(f'<text x="{x}" y="{y+14}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">{ch}</text>')

    # Curved arrows between verbs
    for i in range(4):
        x1, y1, _, _ = positions[i]
        x2, y2, _, _ = positions[(i+1) % 4]
        # Compute control point bowed outward
        mx, my = (x1+x2)/2, (y1+y2)/2
        dx, dy = mx - cx, my - cy
        norm = math.hypot(dx, dy) or 1
        ctrl_x = mx + dx/norm * 50
        ctrl_y = my + dy/norm * 50
        out.append(f'<path d="M{x1} {y1} Q{ctrl_x} {ctrl_y} {x2} {y2}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')

    # Center label
    out.append(f'<text x="{cx}" y="{cy-6}" font-family="{SERIF}" font-size="11" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">this is the practice,</text>')
    out.append(f'<text x="{cx}" y="{cy+10}" font-family="{SERIF}" font-size="11" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">not the project</text>')

    out.append(f'<text x="{w/2}" y="446" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The signals that separated you — the deployed tool, the positioned brand, the published writing — are the costly signals that AI tooling did not make cheap.</text>')
    out.append('</svg>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Map: figures to filenames + chapter context
# ---------------------------------------------------------------------------

FIGURES = [
    # (slug, svg_text, alt, title, ch_file, comment_key)
    ("01-the-creative-engineer-fig-03", fig_1_3(),
     "Two-column schematic showing separating equilibrium where the signal sorts versus pooling equilibrium where it does not",
     "Figure 1.3 — Separating vs. pooling equilibrium",
     "01-the-creative-engineer.md", "two-column schematic"),
    ("01-the-creative-engineer-fig-08", fig_1_8(),
     "Side-by-side mockup of Anthropic's and OpenAI's homepage hero sections, showing identical capability framed for two different audiences",
     "Figure 1.8 — Anthropic / OpenAI brand differentiation",
     "01-the-creative-engineer.md", "Anthropic's and OpenAI's homepage"),
    ("01-the-creative-engineer-fig-12", fig_1_12(),
     "Two GitHub profile mockups — Engineer A reads as Sage shadow / Critic; Engineer B reads as Sage / Teacher",
     "Figure 1.12 — Two GitHub profiles, two archetypes",
     "01-the-creative-engineer.md", "two GitHub profile pages"),
    ("01-the-creative-engineer-fig-13", fig_1_13(),
     "Three-level stack — Spence Mechanism (why), Four-Verb Framework (what), Archetype System (how)",
     "Figure 1.13 — Three frames, one argument",
     "01-the-creative-engineer.md", "three-level stack"),

    ("05-data-pipelines-and-workflow-automation-fig-01", fig_5_1(),
     "Five-node pipeline diagram showing one contract failing and the downstream node degrading rather than crashing",
     "Figure 5.1 — A pipeline as a chain of contracts",
     "05-data-pipelines-and-workflow-automation.md", "horizontal pipeline showing five nodes"),
    ("05-data-pipelines-and-workflow-automation-fig-07", fig_5_7(),
     "Side-by-side comparison of a Python script with interwoven dependencies and an n8n workflow with each contract as a separately-labeled, replaceable node",
     "Figure 5.7 — Python script vs. n8n workflow",
     "05-data-pipelines-and-workflow-automation.md", "side-by-side of two pipeline implementations"),
    ("05-data-pipelines-and-workflow-automation-fig-08", fig_5_8(),
     "Annotated mockup of the n8n node editor — node panel, node with input/output ports, connection between nodes, and the description field where contracts are documented",
     "Figure 5.8 — The n8n node editor",
     "05-data-pipelines-and-workflow-automation.md", "annotated screenshot of the n8n node editor"),
    ("05-data-pipelines-and-workflow-automation-fig-09", fig_5_9(),
     "Madison Intelligence Agent workflow architecture — schedule trigger, parallel ingestion branches, deduplication, LLM scoring, dual outputs",
     "Figure 5.9 — Madison Intelligence Agent architecture",
     "05-data-pipelines-and-workflow-automation.md", "Madison Intelligence Agent's n8n workflow graph"),
    ("05-data-pipelines-and-workflow-automation-fig-11", fig_5_11(),
     "Three-level stack — contract documentation (why), degraded mode design (what), contract monitoring (how)",
     "Figure 5.11 — Pipeline disciplines as a three-level stack",
     "05-data-pipelines-and-workflow-automation.md", "three-level stack echoing the Chapter 1 integration"),

    ("08-personal-brand-path-brand-strategy-fig-02", fig_8_2(),
     "Dependency chain — seven brand components stacked vertically with downward arrows, with Negative Space appearing as the downstream consequence of all seven",
     "Figure 8.2 — Seven components, in the order they constrain each other",
     "08-personal-brand-path-brand-strategy.md", "dependency chain — seven components"),
    ("08-personal-brand-path-brand-strategy-fig-08", fig_8_8(),
     "Circular consistency check — seven brand components arranged in a circle, each adjacent pair connected by an arrow labeled with its consistency question",
     "Figure 8.8 — The internal consistency check",
     "08-personal-brand-path-brand-strategy.md", "circular consistency check"),
    ("08-personal-brand-path-brand-strategy-fig-10", fig_8_10(),
     "Linear flow showing where Chapter 8 sits in the four-verb arc, with the strategy box visually weighted as the scaffold for downstream chapters",
     "Figure 8.10 — Where Chapter 8 sits in the four-verb arc",
     "08-personal-brand-path-brand-strategy.md", "linear flow — Chapter 4 (Career PRD"),

    ("12-professional-presence-and-launch-fig-02", fig_12_2(),
     "The Airbnb argument chain — ten slide boxes connected by 'implies' arrows, showing one continuous logical chain rather than ten independent facts",
     "Figure 12.2 — The Airbnb argument chain",
     "12-professional-presence-and-launch.md", "Airbnb argument chain"),
    ("12-professional-presence-and-launch-fig-11", fig_12_11(),
     "The four-verb loop — Ideate, Build, Brand, Ship arranged in a circle with arrows back to the start, labeled with the chapters where each verb happened",
     "Figure 12.11 — The four-verb loop",
     "12-professional-presence-and-launch.md", "four-verb loop"),
]


def write_svg_and_png(slug, svg_str):
    svg_path = IMG / f"{slug}.svg"
    png_path = IMG / f"{slug}.png"
    svg_path.write_text(svg_str)
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg_str)
    vw, vh = int(m.group(1)), int(m.group(2))
    cairosvg.svg2png(
        bytestring=svg_str.encode("utf-8"),
        output_width=vw * 2,
        output_height=vh * 2,
        write_to=str(png_path),
    )
    return svg_path, png_path


def replace_in_chapter(ch_file, comment_key, slug, alt, title):
    path = CH / ch_file
    text = path.read_text()
    # Find the comment + adjacent placeholder image markdown.
    # Comments here are inline (no closing -->), so our regex must allow that.
    # We replace the comment line AND any adjacent ![Figure ...](...jpg) line.
    # Pattern: comment line, optional blank line, image markdown line.
    comment_pat = re.compile(
        r'<!--\s*→\s*\[(?:IMAGE|FIGURE|DIAGRAM):[^\n]*?'
        + re.escape(comment_key)
        + r'[^\n]*?-->',
    )
    m = comment_pat.search(text)
    if not m:
        print(f"!!! NO MATCH (comment): {ch_file} | key={comment_key!r}")
        return False

    # Look for an adjacent placeholder image markdown (next 2 nonblank lines)
    after = text[m.end():]
    # Check if a placeholder image follows
    img_pat = re.compile(r'^\s*\n+!\[[^\]]*\]\(images/[^)]+\.jpg\)\s*\n', re.MULTILINE)
    img_m = img_pat.match(after)

    new_md = f"![{alt}](images/{slug}.png)\n*{title}*"

    if img_m:
        # Replace comment + blank + image
        new_text = text[:m.start()] + new_md + after[img_m.end():]
    else:
        # Replace just the comment
        new_text = text[:m.start()] + new_md + after

    path.write_text(new_text)
    print(f"  [{ch_file}] {comment_key[:50]} → {slug}.png")
    return True


def main():
    print("=== generating SVGs and PNGs ===")
    for fig in FIGURES:
        slug, svg_text, alt, title, ch_file, comment_key = fig
        write_svg_and_png(slug, svg_text)

    print("\n=== replacing comments in chapter files ===")
    for fig in FIGURES:
        slug, svg_text, alt, title, ch_file, comment_key = fig
        replace_in_chapter(ch_file, comment_key, slug, alt, title)


if __name__ == "__main__":
    main()
