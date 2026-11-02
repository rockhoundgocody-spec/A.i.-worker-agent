## 2026-09-28 - Descriptive Link Labels in Markdown Book Summaries
**Learning:** Generic link anchor texts like `[post]` or `[video]` fail WCAG 2.4.4 (Link Purpose) and confuse screen reader users who navigate links out of context. Using specific labels like `[Reddit Discussion]` and `[YouTube Video]` provides explicit context for external content.
**Action:** When working on markdown document repositories, inspect raw links and replace non-descriptive anchor text with explicit source/destination labels.

## 2026-09-28 - Two-Way Navigation and Breadcrumbs in Markdown Repositories
**Learning:** In static markdown documentation repositories without web chrome or breadcrumb components, sub-pages without return links create dead-ends for readers and keyboard/screen reader users navigating across documents. Adding clear breadcrumbs like `[← Back to All Summaries](../README.md)` restores two-way orientation and navigation flow.
**Action:** Always verify that hierarchical markdown documentation provides clear return navigation links to parent/index files.
