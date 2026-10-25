## 2026-09-28 - Descriptive Link Labels in Markdown Book Summaries
**Learning:** Generic link anchor texts like `[post]` or `[video]` fail WCAG 2.4.4 (Link Purpose) and confuse screen reader users who navigate links out of context. Using specific labels like `[Reddit Discussion]` and `[YouTube Video]` provides explicit context for external content.
**Action:** When working on markdown document repositories, inspect raw links and replace non-descriptive anchor text with explicit source/destination labels.

## 2026-09-28 - Breadcrumb Navigation in Markdown Document Repositories
**Learning:** In markdown document repositories lacking frontend UI navigation bars, users navigating into child documents lose spatial context and must rely on browser controls to return to the root index. Adding a top breadcrumb/back-link (`[← Back to All Summaries](../README.md)`) improves navigation efficiency and spatial orientation for both visual and screen reader users.
**Action:** Always include top back-links/breadcrumbs pointing to the root index in multi-page markdown documentation repositories.
