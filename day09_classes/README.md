## Day 09 — Classes for Data Modeling (OOP Basics Applied)

### Context

As data science projects grow, representing data only as dictionaries and functions
becomes hard to maintain. Real-world libraries use **classes** to bundle data and
behavior together in a clean, extensible way.

Day 09 focuses on practicing **applied object-oriented programming** by modeling
a single energy sensor record as a Python class.

---

## Objective

The goal of this day was to:

- Understand how classes are used in real data science codebases
- Model a single energy record using a class
- Move validation and normalization logic into object methods
- Practice writing clean, readable, library-style code

---

## Task — EnergyRecord Class

### What was implemented

An `EnergyRecord` class was created to represent a single energy sensor reading.
The class encapsulates:

- Raw data (`site_id`, `timestamp`, `demand_kw`)
- Validation logic
- Normalization logic
- Exporting the record as a dictionary

This approach mirrors how data objects are designed in professional data science
and energy analytics libraries.

---

## Key Learnings

- Classes help organize data and behavior together
- Record-level logic belongs with the record itself
- Clean class design improves readability and reuse
- Object-oriented design supports scalable pipelines

---

This day focuses on **foundational OOP concepts** applied to data science,
not on advanced inheritance or patterns.
