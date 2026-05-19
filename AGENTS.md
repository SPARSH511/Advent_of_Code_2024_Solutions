# AGENTS.md

## Purpose

Defines operational rules for all agents, contributors, and automation systems working on this repository.

Main objectives:
- deterministic engineering
- reproducible processing
- traceable execution
- documented failures
- non-repeating mistakes

---

# Core Rule

## NEVER REPEAT THE SAME FAILURE TWICE

If any issue occurs during implementation, it MUST be:
1. documented
2. root-caused
3. fixed
4. prevention-recorded

before continuing.

---

# Mandatory Failure Documentation

Every issue must contain:

```text
Issue
Root Cause
Affected Components
Fix Applied
Preventive Measure
Regression Test Added
```

All recurring failures must be documented inside:

```text
/docs/engineering/failure_patterns.md
```

---

# Engineering Principles

## Determinism First

Avoid:
- nondeterministic ordering
- hidden state
- unstable matching
- random processing behavior

All outputs must be reproducible.

---

# Explainability Mandatory

Every comparison result must explain:
- why a match occurred
- similarity method used
- confidence score
- source locations

---

# Full Traceability

Every pipeline stage must emit structured events.

No silent transformations allowed.

---

# Streaming Over Loading

Never load entire PDFs into memory when avoidable.

Prefer:
- generators
- iterators
- streaming pipelines

---

# Event Sourcing Required

All comparison operations must emit append-only events.

No mutation-only workflows allowed.

---

# PDF Parsing Rules

Assume PDFs may contain:
- corrupt objects
- malformed fonts
- invalid metadata
- missing text layers
- broken layouts

Never trust PDF structure blindly.

---

# Repository Structure

```text
app/
 ├── api/
 ├── extraction/
 ├── normalization/
 ├── structure/
 ├── alignment/
 ├── fingerprinting/
 ├── similarity/
 ├── diffing/
 ├── reporting/
 ├── traceability/
 ├── workers/
 └── storage/
```

---

# Comparison Invariants

## Invariant 1
Every diff must map to source coordinates.

## Invariant 2
Every sentence alignment must include confidence scores.

## Invariant 3
Every section must preserve hierarchy lineage.

## Invariant 4
All events must remain append-only.

---

# Table Diff Rules

Never flatten tables into plain text before diffing.

Preserve:
- rows
- columns
- headers
- merged cells

---

# OCR Rules

OCR output must always include confidence metadata.

Example:

```json
{
  "ocr": true,
  "ocr_confidence": 0.82
}
```

---

# Matching Pipeline

```text
Candidate Retrieval
 → Alignment
 → Detailed Diff
```

Never run expensive global diffs directly.

---

# Performance Rules

Avoid O(N²) comparisons whenever possible.

Prefer:
- hashing
- indexing
- batching
- locality-sensitive hashing

---

# Mandatory Tests

Required:
- unit tests
- regression tests
- malformed PDF tests
- OCR tests
- alignment tests
- table diff tests
- performance tests

---

# Regression Policy

Every production bug must include:
1. failing test
2. root-cause note
3. prevention note

before merge approval.

---

# Forbidden Practices

Never use:
- silent retries
- blanket exceptions
- mutable shared state
- hidden caching
- giant orchestration functions

---

# Final Principle

Correctness and traceability are more important than raw speed.

A slower deterministic system is preferred over a faster opaque system.
