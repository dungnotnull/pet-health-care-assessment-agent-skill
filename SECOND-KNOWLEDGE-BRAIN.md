# SECOND-KNOWLEDGE-BRAIN.md — Pet Health Care & Assessment (per species)

> Self-improving domain knowledge base for `pet-health-care-assessment` (idea #82, cluster `lifestyle-personal`).
> Grown weekly by `tools/knowledge_updater.py`. Last manual seed: 2026-06-18.

## Core Concepts & Frameworks
This skill grounds every judgment in named, citable methodologies:

| Framework / Method | Type | Role in this skill |
|--------------------|------|--------------------|
| AAHA life-stage care guidelines | core methodology | applied in scoring |
| WSAVA nutrition & body-condition scoring | core methodology | applied in scoring |
| Vaccination core/non-core schedules (WSAVA/AAHA) | core methodology | applied in scoring |
| Species-specific welfare (Five Domains model) | core methodology | applied in scoring |
| Preventive-care checklists | core methodology | applied in scoring |
| Triage red-flag protocols | core methodology | applied in scoring |

### Scoring Dimensions
1. Nutrition & body condition
2. Preventive care & vaccination
3. Symptom / red-flag screening
4. Behavior & enrichment
5. Environment & husbandry
6. Life-stage appropriateness

## Key Research Papers
| Title | Authors | Year | Venue | DOI/Link | Relevance |
|-------|---------|------|-------|----------|-----------|
| _(seed pending first crawl)_ | — | — | q-bio.QM | — | Establish baseline state-of-the-art |

## State-of-the-Art Methods & Tools
- Apply the highest-tier framework available for each dimension.
- Prefer current standards and benchmarks over legacy heuristics.
- Cross-check at least two independent sources for any quantitative claim.

## Authoritative Data Sources
- WSAVA & AAHA guidelines
- Merck Veterinary Manual
- PubMed veterinary medicine
- ASPCA/AVMA owner resources
- species breed databases
- ArXiv categories: q-bio.QM

## Analytical Frameworks (world-renowned)
- AAHA life-stage care guidelines
- WSAVA nutrition & body-condition scoring
- Vaccination core/non-core schedules (WSAVA/AAHA)
- Species-specific welfare (Five Domains model)
- Preventive-care checklists
- Triage red-flag protocols

## Self-Update Protocol
- **Tool:** `tools/knowledge_updater.py` (crawl4ai)
- **Sources:** ArXiv (q-bio.QM) + domain URLs above
- **Search queries:** companion animal preventive care; pet nutrition body condition; veterinary vaccination schedule
- **Frequency:** weekly (cron)
- **Append format:** `| Title | Authors | Year | Venue | DOI/URL | Relevance |` rows + dated log entry
- **Dedup:** skip entries whose URL/DOI hash already exists

## Knowledge Update Log
- **2026-06-18** — Seeded knowledge base: 6 frameworks, 6 scoring dimensions, 5 authoritative sources registered. Awaiting first automated crawl.
