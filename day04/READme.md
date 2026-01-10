## Day 04 — Time-Based Feature Engineering

### Context

Time is one of the most important dimensions in data science, especially for domains like
energy systems, demand forecasting, mobility, and user behavior analysis.

Raw timestamps are not directly useful for machine learning models.  
They must first be transformed into **meaningful, structured features** that capture temporal patterns.

---

## Objectives

The goal of Day 04 is to convert raw time-stamped energy data into **model-ready time features** by:

- Extracting useful components from timestamps
- Aggregating demand over time buckets
- Encoding domain knowledge as explicit features

This mirrors the preprocessing steps used in real-world time-series ML pipelines.

---

## Task 1 — Hour Feature Extraction

### Problem

Energy readings arrive with timestamps as strings, which are not suitable for analysis or modeling.

### Solution

- Parsed timestamp strings using Python’s `datetime` library
- Extracted the `hour` component as a numerical feature
- Created a new dataset without mutating the original input

### Outcome

Each record now contains an explicit `hour` feature, enabling downstream grouping and analysis.

---

## Task 2 — Aggregate Demand by Hour

### Problem

Individual readings do not reveal temporal demand patterns.

### Solution

- Grouped records by the extracted `hour`
- Aggregated energy demand using a dictionary accumulator
- Generated a compact representation of hourly demand distribution

### Outcome

A time-based feature mapping hours of the day to total energy demand.

---

## Task 3 — Peak vs Off-Peak Labeling

### Problem

Models benefit from domain-informed features rather than raw time values.

### Business Rule

- Peak hours: 18 to 22 (inclusive)
- Off-peak hours: all other times

### Solution

- Applied domain logic to label each record with a binary `is_peak` feature
- Encoded expert knowledge directly into the dataset

### Outcome

Each data point now explicitly indicates whether it belongs to a peak demand period.

---

## Why This Matters for Data Science

The steps in Day 04 demonstrate how:

- Raw timestamps are transformed into learnable features
- Temporal patterns are surfaced before modeling
- Domain knowledge is incorporated without hard-coding it into models

This approach improves model interpretability, performance, and robustness.

---

## Key Learnings

- `datetime` enables time to be treated as structured data, not text
- Feature engineering is as important as model selection
- Clean, non-mutating pipelines are critical for reliable data science workflows
