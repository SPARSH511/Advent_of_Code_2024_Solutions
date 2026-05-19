
# PRD — Enterprise Deterministic Document Comparison Platform

Version: 1.0
Status: Draft
Target Users:
- Legal teams
- Compliance teams
- Financial auditors
- Enterprise procurement systems
- Internal policy governance teams
- Enterprise contract review systems

---

# 1. Executive Summary

Build a production-grade deterministic document comparison platform capable of comparing:

- 10+ PDFs simultaneously
- 100+ pages per PDF
- scanned and digital PDFs
- deeply structured documents
- tables
- reordered clauses
- moved sections
- near-duplicate content

WITHOUT using:
- LLMs
- GenAI
- embeddings APIs
- transformer inference
- semantic generation systems

The platform must provide:
- full traceability
- deterministic reproducibility
- section-aware diffing
- sentence alignment
- table-aware comparison
- structural matching
- audit logs
- event sourcing
- coordinate-level provenance

The platform should behave similarly to:
- Litera Compare
- Workshare Compare
- iManage Compare

while remaining fully deterministic and explainable.

---

# 2. Problem Statement

Traditional text diff systems fail on enterprise PDFs because PDFs are layout-driven documents rather than semantic documents.

Naive diff systems fail to:
- preserve structure
- detect moved clauses
- align sections
- compare tables correctly
- handle OCR noise
- preserve provenance
- scale beyond small documents

The goal is to build a deterministic document intelligence engine that reconstructs semantic structure from visual PDFs and performs hierarchical comparisons.

---

# 3. Core Design Philosophy

The system is NOT:
- a page comparator
- a text comparator
- a regex diff utility

The system IS:
- a hierarchical document reconstruction engine
- a structural alignment engine
- a traceable comparison engine

Core principle:

Alignment quality > token diff quality

---

# 4. High-Level Architecture

```text
PDF Input
 ↓
PDF Validation
 ↓
OCR Detection
 ↓
Text + Layout Extraction
 ↓
Normalization
 ↓
Reading Order Reconstruction
 ↓
Document DOM Construction
 ↓
Structural Parsing
 ↓
Fingerprinting
 ↓
Candidate Retrieval
 ↓
Section Alignment
 ↓
Paragraph Alignment
 ↓
Sentence Alignment
 ↓
Table Alignment
 ↓
Token Diff
 ↓
Traceability Event Emission
 ↓
Report Rendering
 ↓
Search Indexing
```

---

# 5. Core Requirements

# 5.1 Full Traceability

Every comparison output MUST explain:
- where content originated
- why two blocks matched
- what algorithm matched them
- confidence score
- coordinates
- structural lineage
- OCR confidence

Example:

```json
{
  "source_document": "A.pdf",
  "target_document": "B.pdf",
  "source_page": 12,
  "target_page": 14,
  "source_section": "Termination",
  "target_section": "Termination",
  "match_algorithm": "tfidf+rapidfuzz",
  "similarity_score": 0.93,
  "diff_type": "modified",
  "bbox_source": [0,0,100,20],
  "bbox_target": [0,0,100,20]
}
```

Traceability is a FIRST-CLASS SYSTEM.

Not a reporting layer.

---

# 5.2 Structural Reconstruction

The platform must reconstruct:
- sections
- subsections
- paragraphs
- bullet lists
- numbered lists
- tables
- headers
- footers
- page numbers

from visual PDF layouts.

---

# 5.3 Sentence Alignment

The platform must:
- align reordered sentences
- detect near-duplicates
- avoid greedy matching
- preserve locality
- support bipartite optimal assignment

Sentence alignment is mandatory before token diffing.

---

# 5.4 Section-Aware Diffing

Diffing must NEVER occur:
- page ↔ page

Diffing must ALWAYS occur:
- section ↔ section
- paragraph ↔ paragraph
- sentence ↔ sentence

The system must detect:
- moved sections
- renamed sections
- reordered clauses

without treating them as deletions.

---

# 5.5 Table-Aware Diffing

Tables must preserve:
- rows
- columns
- merged cells
- headers
- structural lineage

The system must:
- align rows
- align columns
- diff cells individually

Tables must NEVER be flattened into plain text before comparison.

---

# 5.6 OCR Handling

The platform must:
- detect scanned PDFs
- OCR only when necessary
- preserve OCR confidence metadata
- support OCR fallback retries
- preserve coordinate mapping after OCR

OCR output is considered low-confidence input.

---

# 6. Internal Document Model (DOM)

The system must create an internal semantic DOM.

Example:

```text
Document
 ├── Metadata
 ├── Pages
 │    ├── Blocks
 │    │    ├── Sentences
 │    │    ├── Tables
 │    │    ├── Lists
 │    │    └── Headers
```

---

# 6.1 Required Models

```python
Document
Page
Block
Sentence
Table
Cell
Section
Alignment
Diff
Event
```

---

# 6.2 Structural Metadata

Every block must contain:
- block id
- page number
- coordinates
- section lineage
- font metadata
- OCR metadata
- reading order index

---

# 7. Algorithms

# 7.1 Candidate Retrieval

Purpose:
Avoid O(N²) comparisons.

Algorithms:
- MinHash
- SimHash
- LSH
- TF-IDF retrieval

---

# 7.2 Similarity Scoring

Signals:
- heading similarity
- hierarchy similarity
- parent similarity
- position similarity
- token similarity
- fuzzy similarity

---

# 7.3 Sentence Matching

Must use:
- Hungarian Algorithm
- bipartite assignment

Must NOT use:
- greedy matching

---

# 7.4 Diff Engine

Required:
- insertion detection
- deletion detection
- movement detection
- modification detection

Preferred library:
- diff-match-patch

---

# 8. Technology Stack

| Layer | Technology |
|---|---|
| API | FastAPI |
| Queue | Celery |
| Broker | Redis |
| Database | PostgreSQL |
| Search | Elasticsearch/OpenSearch |
| OCR | OCRmyPDF + Tesseract |
| Parsing | PyMuPDF |
| Tables | Camelot |
| Similarity | RapidFuzz |
| ML-Free Retrieval | scikit-learn |
| Fingerprinting | datasketch |
| Assignment | SciPy |
| Reporting | Jinja2 |

---

# 9. Repository Structure

```text
app/
 ├── api/
 ├── extraction/
 ├── normalization/
 ├── reading_order/
 ├── structure/
 ├── alignment/
 ├── fingerprinting/
 ├── retrieval/
 ├── diffing/
 ├── reporting/
 ├── traceability/
 ├── indexing/
 ├── workers/
 └── storage/
```

---

# 10. Traceability Event System

Every pipeline stage emits append-only events.

Example events:
- pdf_loaded
- extraction_completed
- section_detected
- sentence_matched
- table_aligned
- diff_generated

---

# 11. Storage Design

# PostgreSQL

Tables:
- documents
- pages
- sections
- blocks
- sentences
- tables
- alignments
- diffs
- events

---

# Elasticsearch/OpenSearch

Indexes:
- block_index
- sentence_index
- section_index
- fingerprint_index

---

# 12. Scalability Requirements

Minimum scale:
- 1000+ total pages
- concurrent jobs
- asynchronous processing

Must support:
- horizontal workers
- distributed queues
- streaming extraction

---

# 13. Performance Constraints

Must avoid:
- O(N²) global comparisons
- full-memory PDF loading
- monolithic diffing

Must use:
- batching
- caching
- indexing
- candidate filtering

---

# 14. Security Requirements

Mandatory:
- MIME validation
- file size limits
- parser sandboxing
- worker isolation
- DOS protection
- timeout enforcement

---

# 15. Observability

Mandatory:
- structured JSON logs
- distributed tracing
- metrics
- event auditing

Metrics:
- OCR failures
- extraction latency
- alignment latency
- queue depth
- memory usage
- worker crashes

---

# 16. Failure Recovery

Must support:
- resumable jobs
- checkpointing
- idempotent retries
- dead-letter queues

---

# 17. Non-Functional Requirements

# Determinism

Given same inputs:
- outputs MUST remain identical

# Explainability

Every match must explain:
- why it matched
- score
- algorithm
- provenance

# Auditability

Every transformation must be logged.

---

# 18. Future Extensions

Future roadmap:
- DOCX comparison
- XLSX diffing
- PowerPoint comparison
- clause classification
- policy validation
- collaborative review UI



# ENTERPRISE ADDENDUM — Production-Scale Requirements

This section extends the PRD for enterprise deployment readiness.

---

# 26. Multi-Tenant Architecture

The platform MUST support:
- multiple organizations
- isolated tenant storage
- isolated search indexes
- isolated queues
- isolated audit trails
- isolated encryption keys

Tenant isolation is mandatory.

No cross-tenant visibility allowed.

---

# 27. Authentication & Identity

Mandatory integrations:
- Microsoft SSO (Azure AD / Entra ID)
- SAML 2.0
- OAuth2/OIDC
- Google Workspace SSO
- Okta
- Ping Identity

---

# 28. RBAC (Role-Based Access Control)

Mandatory roles:
- Platform Admin
- Tenant Admin
- Reviewer
- Auditor
- Read-only User
- API Client

Permissions must support:
- document upload
- comparison creation
- report export
- audit log access
- admin operations

---

# 29. Enterprise Security

Mandatory:
- encryption at rest
- encryption in transit
- signed URLs
- short-lived access tokens
- secrets management
- key rotation
- audit trails
- immutable logs

Recommended:
- Vault integration
- AWS KMS / Azure Key Vault

---

# 30. Compliance Requirements

Target future compatibility:
- SOC2
- ISO 27001
- HIPAA-ready architecture
- GDPR readiness
- enterprise retention policies

---

# 31. Data Retention Policies

Must support:
- tenant-configurable retention
- soft delete
- hard delete
- legal hold
- archival workflows

---

# 32. Object Storage

Documents should NOT be stored in PostgreSQL.

Use:
- S3-compatible object storage
- Azure Blob Storage
- MinIO

Store only metadata in DB.

---

# 33. Search Isolation

Each tenant must have:
- isolated indexes
OR
- strict index-level filtering

Search leakage across tenants is forbidden.

---

# 34. Queue Isolation

Large tenants must not starve smaller tenants.

Mandatory:
- tenant-aware queues
- fair scheduling
- rate limiting
- worker quotas

---

# 35. API Design

Architecture:
- REST-first
- async job APIs
- webhook support
- pagination
- versioned APIs

Endpoints:
- upload
- compare
- status
- reports
- events
- audit
- search

---

# 36. WebSocket / Live Updates

The UI must support:
- live processing updates
- streaming status
- progress events
- live diff rendering

---

# 37. Frontend Requirements

Frontend should support:
- side-by-side document viewing
- synchronized scrolling
- highlighted diffs
- section tree navigation
- table visualization
- traceability inspection
- audit trail inspection

Recommended:
- React
- TypeScript

---

# 38. Distributed Processing

Workers must support:
- horizontal scaling
- Kubernetes autoscaling
- distributed OCR
- distributed indexing
- distributed comparison jobs

---

# 39. Workflow Orchestration

Long-running jobs require:
- checkpoints
- resumability
- dead-letter queues
- retry isolation
- backpressure handling

---

# 40. Caching Strategy

Mandatory cache layers:
- OCR cache
- extraction cache
- fingerprint cache
- TF-IDF cache
- sentence token cache
- similarity cache

---

# 41. Read/Write Separation

Enterprise deployment should support:
- DB replicas
- read scaling
- search scaling
- cache scaling

---

# 42. Disaster Recovery

Mandatory:
- backups
- PITR support
- regional redundancy
- recovery testing
- restore validation

---

# 43. Observability Stack

Recommended:
- OpenTelemetry
- Prometheus
- Grafana
- Loki
- Jaeger

Mandatory:
- tracing
- metrics
- logs
- correlation IDs

---

# 44. Correlation IDs

Every request and event MUST contain:
- request_id
- job_id
- tenant_id
- correlation_id

This is mandatory for enterprise debugging.

---

# 45. Audit Logging

Audit logs must capture:
- uploads
- downloads
- comparisons
- report exports
- login events
- permission changes
- failed auth attempts

Audit logs must be immutable.

---

# 46. Document Versioning

The system must support:
- version lineage
- repeated comparisons
- historical diffs
- rollback visibility

---

# 47. Scalability Targets

Future-scale targets:
- 100K+ documents
- 1M+ comparison events
- concurrent enterprise tenants
- large OCR workloads

---

# 48. Deployment Strategy

Supported:
- SaaS multi-tenant
- single-tenant cloud
- on-prem enterprise deployment
- air-gapped deployment

---

# 49. Infrastructure-as-Code

Mandatory:
- Terraform
- Helm charts
- Kubernetes manifests
- environment reproducibility

---

# 50. CI/CD Requirements

Mandatory:
- unit tests
- integration tests
- load tests
- regression suites
- security scanning
- SAST
- dependency scanning

---

# 51. PDF Threat Model

Assume malicious PDFs may contain:
- decompression bombs
- malformed objects
- parser exploits
- malicious metadata
- infinite object recursion

All parsing must occur in sandboxed workers.

---

# 52. Enterprise SLA Targets

Target:
- 99.9% uptime
- predictable processing latency
- bounded queue wait times

---

# 53. Internal SDK

Create internal SDKs for:
- extraction
- alignment
- diffing
- traceability
- reporting

Avoid tightly coupled services.

---

# 54. Configuration Management

All thresholds must be configurable:
- OCR confidence
- alignment thresholds
- diff thresholds
- retry counts
- queue priorities

Hardcoded heuristics are forbidden.

---

# 55. Feature Flags

Mandatory:
- rollout control
- staged deployments
- tenant-specific enablement
- rollback safety

---

# 56. Search & Retrieval Features

Enterprise users will require:
- clause search
- historical comparison search
- similarity lookup
- changed-section search
- audit retrieval

---

# 57. Explainability UI

Every diff should expose:
- why matched
- algorithm used
- score
- structural lineage
- provenance
- OCR status

---

# 58. Export Formats

Support:
- HTML
- PDF
- JSON
- CSV summaries

Future:
- DOCX exports

---

# 59. Rate Limiting

Mandatory:
- tenant limits
- upload limits
- API throttling
- worker quotas

---

# 60. Enterprise Architecture Principle

This platform is fundamentally:
- a document intelligence infrastructure system
NOT:
- a simple diff viewer

Core engineering priority order:
1. correctness
2. traceability
3. reproducibility
4. scalability
5. performance




# 61. Semantic Chunking & Internal JSON Representation

This is one of the MOST CRITICAL subsystems in the entire platform.

The comparison engine must NEVER operate directly on raw PDF text streams.

The platform must transform PDFs into semantically meaningful structured chunks before:
- indexing
- alignment
- diffing
- traceability
- search
- reporting

The quality of chunking directly determines:
- alignment quality
- traceability quality
- diff quality
- scaling efficiency

Poor chunking destroys enterprise comparison quality.

---

# 61.1 Why Semantic Chunking Matters

Naive chunking approaches fail because:
- PDFs are layout-based
- sentences cross lines/pages
- headers repeat
- tables break text flow
- OCR introduces noise
- clauses may move

The engine must create semantically stable chunks.

---

# 61.2 Chunking Pipeline

```text
Raw PDF
 ↓
Layout Extraction
 ↓
Reading Order Reconstruction
 ↓
Header/Footer Removal
 ↓
Block Detection
 ↓
Structural Classification
 ↓
Sentence Segmentation
 ↓
Section Hierarchy Construction
 ↓
Semantic Chunk Generation
 ↓
Fingerprinting & Indexing
```

---

# 61.3 Chunk Types

Supported chunk types:

- document
- section
- subsection
- paragraph
- sentence
- table
- table_row
- table_cell
- list
- list_item
- header
- footer
- footnote

Each chunk type must preserve:
- coordinates
- lineage
- ordering
- provenance

---

# 61.4 Canonical Chunk Structure

Every chunk MUST follow a canonical schema.

Example:

```json
{
  "chunk_id": "blk_019283",
  "document_id": "doc_001",
  "page": 12,
  "reading_order": 48,
  "chunk_type": "paragraph",
  "section_path": [
    "Payment Terms",
    "Late Fees"
  ],
  "text": "Payment shall be completed within thirty days.",
  "normalized_text": "payment shall be completed within thirty days",
  "bbox": [120, 310, 580, 355],
  "ocr": false,
  "ocr_confidence": null,
  "font_metadata": {
    "font_size": 11,
    "font_name": "TimesNewRoman",
    "is_bold": false
  },
  "fingerprints": {
    "sha256": "...",
    "simhash": "...",
    "minhash": "..."
  }
}
```

---

# 61.5 Sentence-Level Chunk Example

```json
{
  "sentence_id": "sent_8821",
  "parent_block_id": "blk_019283",
  "document_id": "doc_001",
  "page": 12,
  "sentence_index": 2,
  "section_path": [
    "Payment Terms"
  ],
  "text": "Late payments incur additional charges.",
  "tokens": [
    "late",
    "payments",
    "incur",
    "additional",
    "charges"
  ],
  "bbox": [100, 220, 510, 250],
  "fingerprints": {
    "simhash": "...",
    "tfidf_terms": ["late", "payments", "charges"]
  }
}
```

---

# 61.6 Table Chunk Representation

Tables must NEVER become flattened text blobs.

Example:

```json
{
  "table_id": "tbl_221",
  "document_id": "doc_001",
  "page": 19,
  "section_path": [
    "Pricing"
  ],
  "bbox": [80, 100, 550, 420],
  "columns": [
    {
      "column_id": "col_1",
      "header": "Service"
    },
    {
      "column_id": "col_2",
      "header": "Price"
    }
  ],
  "rows": [
    {
      "row_id": "row_1",
      "cells": [
        {
          "cell_id": "cell_1",
          "value": "Premium Support"
        },
        {
          "cell_id": "cell_2",
          "value": "$100"
        }
      ]
    }
  ]
}
```

---

# 61.7 Section Chunk Representation

```json
{
  "section_id": "sec_991",
  "title": "Termination",
  "level": 1,
  "section_path": [
    "Termination"
  ],
  "page_start": 14,
  "page_end": 18,
  "child_sections": [
    "Notice Period",
    "Immediate Termination"
  ],
  "block_references": [
    "blk_991",
    "blk_992"
  ]
}
```

---

# 61.8 Alignment-Friendly Chunking

Chunks MUST be optimized for:
- deterministic matching
- locality preservation
- movement detection
- structural lineage

Chunking should NEVER:
- split mid-sentence
- split inside tables
- split across semantic boundaries

---

# 61.9 Chunk Lineage

Every chunk must preserve ancestry.

Example:

```json
{
  "chunk_id": "sent_8821",
  "parent_block_id": "blk_019283",
  "parent_section_id": "sec_992",
  "document_id": "doc_001"
}
```

This is mandatory for:
- traceability
- explainability
- audit reconstruction

---

# 61.10 Chunk-Level Fingerprinting

Every chunk must generate:
- exact hash
- fuzzy fingerprint
- retrieval fingerprint

Required:
- SHA256
- SimHash
- MinHash

This enables:
- fast retrieval
- incremental comparison
- cache reuse

---

# 61.11 Incremental Reuse

Chunk fingerprints must allow:
- repeated comparison reuse
- cache reuse
- deduplication
- historical lineage tracking

This is critical at enterprise scale.

---

# 61.12 Chunking Failure Modes

Known failure modes:
- OCR line fragmentation
- header bleed-through
- multi-column ordering errors
- broken table extraction
- repeated footers
- merged paragraphs

Each failure mode must:
- be documented
- have regression tests
- have monitoring metrics

Mandatory location:

```text
/docs/engineering/chunking_failure_patterns.md
```

---

# 61.13 Chunking Invariants

Invariant 1:
Chunks must preserve reading order.

Invariant 2:
Chunks must preserve source coordinates.

Invariant 3:
Chunks must preserve structural lineage.

Invariant 4:
Tables must preserve cell structure.

Invariant 5:
Sentence chunks must remain semantically complete.

---

# 61.14 Enterprise Principle

The internal semantic chunking layer is the FOUNDATION of the entire platform.

All downstream quality depends on:
- chunk quality
- lineage quality
- structural reconstruction quality

Chunking correctness is more important than diff visualization quality.
