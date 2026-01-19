## Day 13 — Object-Oriented Programming with Energy Assets

### Context

Energy and climate-tech systems often deal with multiple types of assets that share
common properties but behave differently. Clean software design in such systems relies
on **Object-Oriented Programming (OOP)** concepts such as inheritance and polymorphism.

Day 13 focuses on applying these concepts using **real energy-domain examples** rather
than abstract or toy problems.

---

## Objective

The goals of this day were to:

- Practice class-based design in a data science context
- Apply inheritance using a shared base class
- Override behavior in child classes
- Understand polymorphism through a common interface

---

## System Design

### Base Class — `EnergyAsset`

A generic base class representing an energy-related asset, containing:
- Common attributes (`name`, `location`, `capacity_kw`)
- A shared method interface (`estimate_annual_output`)
- A strict contract enforced via `NotImplementedError`

---

### Implemented Child Classes

#### `BiomassPlant`
- Represents biomass-based electricity generation
- Annual output estimated in **kWh/year**
- Depends on capacity, operating hours, and conversion efficiency

#### `EnergyStorageSystem`
- Represents an energy storage system (battery)
- Annual output estimated as **usable discharged energy**
- Depends on storage capacity and round-trip efficiency

---

## Polymorphism in Practice

Both asset types share the same interface:

```python
asset.estimate_annual_output()
