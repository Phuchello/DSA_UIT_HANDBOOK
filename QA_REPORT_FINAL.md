# FINAL CODEX QA REPORT

## Input Candidate

- Candidate: `master.html` from `IT003_DSA_BOOK.zip`
- Candidate timestamp: 2026-08-13 22:05:50
- Pre-edit SHA-256: `663171A4BA29AF3A8501D979A7786865E9128395E4E5374AD816FB221DE0A8CE`
- Selection basis: `PROJECT_STATE.md` marks Phase 3 complete/content frozen; the archive contains only one top-level HTML candidate, `master.html`.
- Checkpoint: `backup/pre_codex_master.html` and `backup/pre_codex_print.css` created before edits.
- Archive note: `TODO.md` and `SOURCE_AUDIT.md` are referenced by `PROJECT_STATE.md` but are not present in the supplied ZIP. No source re-audit or broad research was performed.

## Files Modified

- `master.html`
- `print.css`
- `build.ps1` (local KaTeX paths and shared cover/TOC classes)
- `PROJECT_STATE.md`
- Added `assets/katex/` (KaTeX 0.16.22 runtime and bundled KaTeX fonts)
- Added `QA_REPORT_FINAL.md`

## Engineering Fixes

- Escaped all raw ampersands so prose and C++ expressions are valid HTML.
- Replaced all CDN/font-network dependencies with local assets and system-safe font stacks.
- Consolidated cover and TOC inline rules into reusable CSS classes.
- Reworked table, code, callout, chapter-header, orphan, and widow break rules for A4 flow.
- Allowed long tables/code blocks to split safely while keeping table rows and headings together.
- Removed the final two-line trailing page by tightening only the list-heavy Exam Toolkit rhythm.
- Added missing standard headers to selected C++ snippets.

## HTML Validation

- UTF-8 strict: PASS; BOM: none; unexpected controls: 0; mojibake/tofu: 0.
- HTML parse: PASS; duplicate IDs: 0; broken anchors: 0; broken local paths: 0.
- TOC anchors `#ch00` through `#ch15`: 16/16 present exactly once.
- Tables: 35; tables without `<th>`: 0.
- Code blocks: 27; nested/unescaped C++ HTML: 0.
- Remote dependencies/network requests: 0.

## C++ Validation

- Toolchain: MinGW g++, C++17, `-Wall -Wextra -Wpedantic -O2`.
- Searching: binary search boundaries, hit/miss, empty input: PASS.
- Sorting: Selection, Interchange, Bubble optimized, Insertion, Binary Insertion, Shell, Heap: PASS on empty, singleton, duplicate, negative, sorted/reverse cases.
- Linked List: empty/one-node, addHead, deleteHead, insertAfter tail, search miss: PASS.
- Stack/Queue: empty pop/dequeue, full push/enqueue, overflow guard, circular wrap-around: PASS.
- BST: search; delete leaf, one-child, two-child; in-order invariant: PASS.
- AVL: LL, RR, LR, RL sequences all produce root 20, left 10, right 30: PASS.
- Heapify and Heap Sort: PASS.
- BFS/DFS: visited-on-enqueue semantics, neighbor order, disconnected component behavior: PASS.
- Dijkstra example: `[0, 3, 2, 8]`: PASS.
- Merge/Quick/Radix helper fragments remain explicitly labeled `Pseudocode Helper`.

## Math / KaTeX Validation

- KaTeX 0.16.22 localized under `assets/katex/`; initialized once.
- Browser render: 490 KaTeX nodes; `.katex-error`: 0; raw/unrendered math delimiters: 0.
- Delimiter parity and key-command scan: PASS.
- Corrected hash formulas to use `\bmod` so `mod` renders as an operator.

## SVG Validation

- Inline SVGs: 15.
- `url(#...)` references: 8 unique; unresolved targets: 0.
- Duplicate/conflicting SVG IDs: 0.
- Full-page review found no clipped labels, missing arrows, overflow, or unreadable node labels.

## Print CSS Changes

- `@page { size: A4 portrait; margin: 18mm 15mm 18mm 15mm; }` retained.
- System fonts: Segoe UI/Noto Sans/Arial; code: Cascadia Code/Consolas/Liberation Mono.
- Cover centered and balanced; TOC remains one compact page.
- Removed forced page breaks from every `h1`; chapter headers now flow without creating half-empty pages.
- Tables repeat headers when split; rows remain intact; code wraps without horizontal clipping.
- SVGs remain responsive within printable width.

## PDF Render Configuration

- Engine: Google Chrome headless.
- Paper: A4; scale: 100%; background graphics: ON.
- Browser headers/footers: OFF; CSS page size preferred.
- Output page size: 594.96 × 841.92 pt (A4 within renderer rounding).

## PDF Page Count

49 pages.

## Full-page QA Findings

- Pass 1 — Structural: rendered all 50 initial pages; found a final callout-only page.
- Pass 2 — Typography/layout: rerendered to 49 pages; no blank/sparse pages, clipping, overflow, tofu, raw math, or broken tables/code.
- Pass 3 — Visual/content spot-check: rerendered all 49 final pages to PNG, reviewed three complete contact sheets, and zoom-reviewed sorting, linked list, BST, AVL, B-Tree, Hash, BFS/DFS, Dijkstra, and Exam Toolkit pages.
- Final automated density scan: sparse pages 0; unexplained large-bottom-gap pages 0 (cover/TOC excluded by design).

## Issues Fixed

- Added cover compiler credit: Võ Trọng Phúc.
- P0: offline KaTeX/CDN dependency; invalid raw ampersands; code/math HTML reliability.
- P1: page-flow rules causing a two-line trailing page; wide-content safeguards; local asset reliability.
- Precision: BST complexity standardized to `O(h)` with balanced/worst qualifiers.
- Precision: Binary Insertion metric tied to the shown implementation; Shell Sort matrix made gap-dependent.
- Precision: Bellman-Ford negative-cycle caveat scoped to cycles reachable from the source.
- Precision: hash `mod` formulas corrected to `\bmod`.
- Verified Interchange Sort remains marked NOT STABLE.

## Remaining Non-blocking Issues

- Visible PDF page numbers are intentionally omitted because Chromium does not reliably support CSS margin-box page counters; browser headers/footers remain disabled to protect layout.
- A few long educational code blocks split across pages, but line order, indentation, contrast, and readability remain intact.

## Final Score

| Category | Score |
| :--- | ---: |
| Content Accuracy | 19/20 |
| UIT Alignment | 15/15 |
| Beginner Clarity | 14/15 |
| Algorithm Intuition | 9/10 |
| Code Quality | 10/10 |
| Exercises | 9.5/10 |
| Visual Explanation | 7.5/8 |
| Exam Usefulness | 5/5 |
| Layout & Print | 4/5 |
| Navigation/Consistency | 2/2 |
| **TOTAL** | **95/100** |

## Release Status

- P0 blockers: 0
- P1 blockers: 0
- Full PDF QA: PASSED
- Release: FINAL
