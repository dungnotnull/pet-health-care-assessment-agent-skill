# CLAUDE.md — Pet Health Care & Assessment (per species)

**Skill name:** `pet-health-care-assessment`
**Tagline:** Pet Health Care & Assessment (per species)
**Source idea:** #82  |  **Cluster:** `lifestyle-personal` (Lifestyle & Personal)
**Current phase:** Phase 2 complete (core sub-skills + harness + quality gates). Phase 3 knowledge pipeline scaffolded.

## Problem This Skill Solves
Owners miss early disease signs and mistime nutrition/vaccination. This skill assesses pet health by species, scores care quality, and routes urgent signs to a vet.

## Harness Flow Summary
1. **Intake / scoping** → `sub-profile-intake.md` gathers context and constraints.
2. **Framework selection** → `sub-safety-screener.md` chooses the named evaluation frameworks for this case.
3. **Research / evidence** → WebSearch + WebFetch pull authoritative sources; fall back to SECOND-KNOWLEDGE-BRAIN.md if offline.
4. **Scoring / analysis** → `sub-framework-selector.md` scores across the 6 dimensions.
5. **Challenge phase** → devil's-advocate review (`sub-improvement-roadmap.md`).
6. **Synthesis** → main harness assembles the final professional deliverable (score + prioritized roadmap).

**Safety gate:** `sub-safety-screener` MUST run before any guidance is produced; crisis/emergency red flags escalate to professional/emergency resources immediately.

## Sub-skills
- `skills/sub-profile-intake.md` — Capture species, breed, age, weight and history with an educational/non-diagnostic disclaimer.
- `skills/sub-safety-screener.md` — Screen for veterinary emergency red flags FIRST and route urgent cases to a vet/ER.
- `skills/sub-framework-selector.md` — Apply the species/life-stage AAHA/WSAVA guideline set.
- `skills/sub-improvement-roadmap.md` — Build a preventive-care, nutrition and vaccination plan with vet-visit triggers.

## Tools Required
- WebSearch, WebFetch (research-first evidence gathering)
- Read, Write (deliverable assembly)
- Bash / Python (run `tools/knowledge_updater.py`)

## Knowledge Sources
- ArXiv categories: q-bio.QM
- Domain sources: WSAVA & AAHA guidelines, Merck Veterinary Manual, PubMed veterinary medicine, ASPCA/AVMA owner resources, species breed databases

## Supporting Python Tools
- `tools/knowledge_updater.py` — crawl4ai pipeline that refreshes `SECOND-KNOWLEDGE-BRAIN.md` weekly.

## Active Development Tasks
- [x] Scaffold folder + 8 required deliverables
- [x] Define 6 named evaluation frameworks
- [x] Implement 4 sub-skills (min 3)
- [ ] Wire shared cluster sub-skills across `lifestyle-personal`
- [ ] First live crawl to seed SECOND-KNOWLEDGE-BRAIN knowledge log

## Reference Docs
- `PROJECT-detail.md` — full technical spec
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — phase roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — self-improving knowledge base
