## 2026-09-28 - Descriptive Link Labels in Markdown Book Summaries
**Learning:** Generic link anchor texts like `[post]` or `[video]` fail WCAG 2.4.4 (Link Purpose) and confuse screen reader users who navigate links out of context. Using specific labels like `[Reddit Discussion]` and `[YouTube Video]` provides explicit context for external content.
**Action:** When working on markdown document repositories, inspect raw links and replace non-descriptive anchor text with explicit source/destination labels.

## 2026-09-28 - Relative Breadcrumb Links in Markdown Repository Documents
**Learning:** Nested markdown summary documents lack built-in navigation headers. Adding explicit relative breadcrumb links at the top of nested files enables intuitive keyboard and screen-reader accessible navigation back to the main index.
**Action:** In pure Markdown document repositories, include relative back-to-index links (`[← Back to All Summaries](../README.md)`) at the top of nested documents.
