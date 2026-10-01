## 2026-09-28 - Descriptive Link Labels in Markdown Book Summaries
**Learning:** Generic link anchor texts like `[post]` or `[video]` fail WCAG 2.4.4 (Link Purpose) and confuse screen reader users who navigate links out of context. Using specific labels like `[Reddit Discussion]` and `[YouTube Video]` provides explicit context for external content.
**Action:** When working on markdown document repositories, inspect raw links and replace non-descriptive anchor text with explicit source/destination labels.

## 2026-10-15 - Top and Bottom Navigation Links for Markdown Document Repositories
**Learning:** Deeply nested markdown documents in repository-based documentation or book summaries lack browser-independent navigation. Adding descriptive `[← Back to All Summaries](../README.md)` links at both the top (breadcrumb) and bottom (footer) improves screen reader and keyboard user orientation and seamless page flow.
**Action:** When working on pure markdown documentation repos, ensure individual sub-documents include dual breadcrumb and footer navigation links back to the main index.
