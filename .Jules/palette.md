## 2026-09-28 - Descriptive Link Labels in Markdown Book Summaries
**Learning:** Generic link anchor texts like `[post]` or `[video]` fail WCAG 2.4.4 (Link Purpose) and confuse screen reader users who navigate links out of context. Using specific labels like `[Reddit Discussion]` and `[YouTube Video]` provides explicit context for external content.
**Action:** When working on markdown document repositories, inspect raw links and replace non-descriptive anchor text with explicit source/destination labels.

## 2026-11-07 - Unordered List Formatting for Consecutive External Links
**Learning:** Consecutive unbulleted link lines in Markdown collapse into a single inline paragraph in standard Markdown renderers, obscuring visual separation and depriving screen reader users of structural list semantics (WCAG 1.3.1).
**Action:** Format consecutive resource links as Markdown unordered list items (`* [Label](url)`) to provide clear visual delimitation and semantic list structure for assistive technologies.
