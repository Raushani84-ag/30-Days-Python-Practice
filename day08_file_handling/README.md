## Day 08 — File Handling & Mini ETL Pipeline

### Context

Real-world data science pipelines often begin with raw files:
sensor logs, CSV exports, or text-based data dumps.
These files frequently contain malformed or incomplete records, and pipelines must
handle such issues **without crashing**.

Day 08 focuses on building a **file-based mini ETL pipeline** using pure Python.

---

## Objectives

The goals of Day 08 were to:

- Read raw data files safely using context managers
- Parse structured records from raw text lines
- Skip malformed records without breaking execution
- Persist cleaned data for downstream processing
- Log parsing errors with clear diagnostic information

---

## Task 1 — Safe File Reading

### What was done
- Read raw energy sensor data line by line using `with open`
- Ensured files are closed safely after reading

### Outcome
A reliable ingestion step that handles raw file input predictably.

---

## Task 2 — Parsing & Error Handling

### What was done
- Parsed each line into structured energy records
- Validated basic formatting rules
- Captured malformed lines along with error reasons and line numbers

### Outcome
Separated valid records from invalid ones without crashing the pipeline.

---

## Task 3 — Writing Clean Output & Logs

### What was done
- Wrote valid, cleaned records to an output file
- Logged parsing errors to a separate processing log
- Composed all steps into a single reproducible pipeline

### Outcome
A complete mini ETL workflow:
Read → Parse → Write Clean Data → Log Errors

---

## Key Learnings

- File handling is a core part of real data pipelines
- Pipelines must tolerate bad data and continue processing
- Clear error logging is essential for debugging and monitoring
- Small, composable functions make pipelines easier to reason about

---

Day 08 emphasizes **robust ingestion and reproducibility**, foundational skills
for applied data science and energy data workflows.
