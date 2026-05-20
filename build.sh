#!/bin/bash
# Build script for the Botspeak book — pandoc → EPUB + HTML
# Run from the book root: cd books/botspeak && ./build.sh
set -e

BOOK_SLUG="branding-and-ai"
METADATA="metadata.yaml"
OUTPUT_DIR="output"
COMBINED="$OUTPUT_DIR/combined.md"
COVER="cover.jpg"

mkdir -p "$OUTPUT_DIR"

# Compile chapters in filename order:
#   00-frontmatter.md
#   00-the-citation-that-wasnt.md  (intro / Ch 0)
#   01-...-13-...                   (chapters 1–13)
#   99-back-matter.md
#
# Pass chapter files directly to pandoc rather than cat-concatenating them.
# Pandoc parses each file separately and joins the resulting ASTs, which
# avoids the case where a horizontal-rule `---` at the end of one chapter
# and a horizontal-rule `---` at the start of the next collide and look
# like a YAML metadata block to the parser.
mapfile -t CHAPTER_FILES < <(ls chapters/*.md)

# Keep a concatenated copy for archival / proofing convenience.
cat "${CHAPTER_FILES[@]}" > "$COMBINED"

# --- EPUB (primary — upload this to KDP) ----------------------------------
EPUB_FLAGS=(
  --from markdown-yaml_metadata_block
  --to epub3
  --metadata-file="$METADATA"
  --css=styles/kindle.css
  --css=styles/kindle-book.css
  --resource-path=.:images:styles
  --toc --toc-depth=2
  --output="$OUTPUT_DIR/$BOOK_SLUG.epub"
)
if [[ -f "$COVER" ]]; then
  EPUB_FLAGS+=(--epub-cover-image="$COVER")
fi
pandoc "${CHAPTER_FILES[@]}" "${EPUB_FLAGS[@]}"

# --- HTML (proofing — mirrors EPUB cascade exactly) -----------------------
pandoc "${CHAPTER_FILES[@]}" \
  --from markdown-yaml_metadata_block \
  --to html5 \
  --standalone \
  --metadata-file="$METADATA" \
  --css=styles/kindle.css \
  --css=styles/kindle-book.css \
  --resource-path=.:images:styles \
  --toc \
  --output="$OUTPUT_DIR/$BOOK_SLUG.html"

echo "Built: $OUTPUT_DIR/$BOOK_SLUG.epub"
echo "Built: $OUTPUT_DIR/$BOOK_SLUG.html"

if [[ ! -f "$COVER" ]]; then
  echo
  echo "Note: $COVER not found — EPUB built without a cover image."
  echo "      Add a 1600x2560 JPEG cover to $COVER and rebuild for KDP upload."
fi
