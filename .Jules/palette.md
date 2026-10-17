## 2026-09-28 - Descriptive Link Labels in Markdown Book Summaries
**Learning:** Generic link anchor texts like `[post]` or `[video]` fail WCAG 2.4.4 (Link Purpose) and confuse screen reader users who navigate links out of context. Using specific labels like `[Reddit Discussion]` and `[YouTube Video]` provides explicit context for external content.
**Action:** When working on markdown document repositories, inspect raw links and replace non-descriptive anchor text with explicit source/destination labels.

## 2026-10-17 - Breadcrumb Navigation and List Formatting in Markdown Documents
**Learning:** In markdown document repositories without UI frameworks, standalone nested documents often lack wayfinding back to the index page. Consecutive raw link lines without list syntax collapse into unorganized inline text in standard Markdown renderers.
**Action:** Always add top-level breadcrumb back links (`[← Back to All Summaries](../README.md)`) and wrap multiple resource links in bullet lists (`* [Label](url)`) to provide accessible list semantics (WCAG 1.3.1).
