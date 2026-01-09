## Day 03 — Metadata & Configuration Handling (Data Science Workflow)

### Context

In real-world data science projects, raw datasets rarely contain all the information required for modeling.
Measurements often arrive with only identifiers, while **contextual information (metadata)** lives separately
in configuration files, databases, or spreadsheets.

This day focuses on **joining raw data with metadata and applying business rules** — a critical step before
feature engineering or modeling.

---

## Task 1 — Enrich Energy Data with Metadata

### Problem

Energy consumption readings contain only:
- site identifiers
- numeric demand values

However, meaningful analysis requires additional context such as:
- location
- site type
- capacity or category

### Objective

Merge raw energy readings with site metadata to create **enriched, model-ready records**.

### Key Rules Implemented

- Metadata is looked up using `site_id`
- Records with missing metadata are safely skipped
- Original input data is not mutated
- New enriched records are created explicitly

### Concepts Used

- Dictionary lookup (`dict.get`)
- Safe data merging (`copy` + `update`)
- Defensive programming
- List accumulation

---

## Task 2 — Filter Data Using Business Rules

### Problem

Not all site types are relevant for every analysis.
For example, a forecasting model may focus only on **commercial and industrial** consumers.

### Objective

Filter enriched data based on a predefined set of **allowed site types**.

### Business Rule

Only records where:
```text
site_type ∈ {"commercial", "industrial"}
