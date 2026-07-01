# Pet Health Care & Assessment (per species)

> A research-first, framework-based companion animal care evaluation skill for Claude Code

**Idea #82** · **Cluster**: `lifestyle-personal` · **Tagline**: Pet Health Care & Assessment (per species)

---

## Overview

This skill provides comprehensive, evidence-based evaluation of pet care across multiple dimensions. It applies recognized veterinary frameworks (AAHA, WSAVA, Five Domains Model) to assess current care practices and generates a prioritized improvement roadmap.

### What It Does

1. **Comprehensive Intake**: Collects detailed pet profile including species, breed, age, health history, and current care practices
2. **Safety Screening**: Checks for veterinary emergency red flags before providing any guidance
3. **Evidence-Based Scoring**: Evaluates care across 6 dimensions using authoritative veterinary frameworks
4. **Challenge Phase**: Applies devil's-advocate review to validate findings
5. **Prioritized Roadmap**: Generates actionable recommendations with impact/effort analysis

### What It Doesn't Do

- **Medical diagnosis**: This is educational guidance only, not veterinary care
- **Treatment recommendations**: Always consult a licensed veterinarian for medical issues
- **Emergency care**: Emergencies require immediate veterinary attention

---

## Quick Start

### Using the Skill

```bash
# Invoke the skill
claude skill pet-health-care-assessment

# Example requests:
"Assess my dog's health care"
"How can I improve my cat's care?"
"Evaluate my rabbit's care practices"
"What should I prioritize for my pet's health?"
```

### What to Expect

1. **Disclaimer**: You'll be asked to acknowledge the educational nature of the assessment
2. **Intake Questions**: The skill will ask about your pet's demographics, health history, and current care
3. **Safety Check**: The skill will screen for any emergency conditions
4. **Evaluation**: Comprehensive assessment across 6 care dimensions
5. **Recommendations**: Prioritized roadmap for improvement opportunities

---

## Skills Structure

```
pet-health-care-assessment/
├── skills/
│   ├── main.md                    # Main harness and workflow
│   ├── sub-profile-intake.md      # Demographic and history collection
│   ├── sub-safety-screener.md     # Emergency red flag detection
│   ├── sub-framework-selector.md  # Evidence-based scoring engine
│   └── sub-improvement-roadmap.md # Challenge phase and recommendations
├── tools/
│   ├── knowledge_updater.py       # Weekly knowledge base refresh
│   └── requirements.txt           # Python dependencies
├── tests/
│   └── test-scenarios.md          # Comprehensive test scenarios
├── CLAUDE.md                      # Project instructions
├── CLUSTER-INTEGRATION.md         # Cross-skill compatibility
├── PROJECT-detail.md              # Technical specification
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md  # Phase tracking
├── SECOND-KNOWLEDGE-BRAIN.md      # Self-improving knowledge base
└── README.md                      # This file
```

---

## The Six Evaluation Dimensions

### 1. Nutrition & Body Condition
**Frameworks**: WSAVA Nutrition Guidelines, Body Condition Scoring (BCS)
- Diet quality and appropriateness
- Body condition assessment
- Life-stage nutrition
- Supplement and treat evaluation

### 2. Preventive Care & Vaccination
**Frameworks**: AAHA/WSAVA Vaccination Guidelines, AAHA Life-Stage Care
- Core vaccination status
- Parasite prevention
- Wellness exam frequency
- Dental care
- Age-appropriate screenings

### 3. Symptom/Red-Flag Screening
**Frameworks**: AAHA Health Screening, Triage Protocols
- Current symptom evaluation
- Health status assessment
- Early warning sign detection

### 4. Behavior & Enrichment
**Frameworks**: Five Domains Model (Behavior Domain), AAHA Behavior Guidelines
- Species-typical behaviors
- Mental enrichment
- Behavioral health
- Training and socialization

### 5. Environment & Husbandry
**Frameworks**: Five Domains Model (Environment Domain), Species-Specific Standards
- Housing appropriateness
- Temperature and environmental control
- Safety considerations
- Cleanliness and hygiene

### 6. Life-Stage Appropriateness
**Frameworks**: AAHA Life-Stage Care Guidelines
- Age-appropriate care
- Life-stage specific needs
- Preventive care timing
- Senior/geriatric considerations

---

## Scoring Scale

| Score Range | Grade | Interpretation |
|-------------|-------|----------------|
| 4.5-5.0 | Excellent | Optimal care across all dimensions |
| 4.0-4.49 | Very Good | High-quality care with minor improvements possible |
| 3.5-3.99 | Good | Solid care with some improvement opportunities |
| 3.0-3.49 | Fair | Adequate care with several improvement needs |
| 2.0-2.99 | Poor | Significant gaps requiring attention |
| 1.0-1.99 | Serious | Major concerns needing urgent attention |
| 0.0-0.99 | Critical | Emergency intervention required |

---

## Veterinary Frameworks Applied

### Primary Frameworks

| Framework | Source | Application |
|-----------|--------|-------------|
| AAHA Life-Stage Care Guidelines | American Animal Hospital Association | Dogs and cats |
| WSAVA Nutrition Guidelines | World Small Animal Veterinary Association | Nutritional assessment |
| WSAVA/AAHA Vaccination Guidelines | WSAVA and AAHA | Vaccination schedules |
| Five Domains Model | Mellor et al. | Welfare assessment |
| Triage Red-Flag Protocols | Veterinary emergency standards | Emergency screening |

### Species-Specific Frameworks

- **Dogs**: AAHA Canine Guidelines, WSAVA Nutrition
- **Cats**: AAHA Feline Guidelines, AAFP Nutrition
- **Rabbits**: RCVS/BSAVA Rabbit Welfare, House Rabbit Society
- **Birds**: AAav (Association of Avian Veterinarians)
- **Reptiles**: ARV (Association of Reptile Veterinarians)

---

## Safety Features

### Emergency Detection

The skill screens for emergency conditions BEFORE providing any guidance:

**Life-Threatening Indicators**:
- Respiratory distress
- Cardiovascular collapse
- Seizures/coma
- GDV/bloat
- Trauma
- Urinary obstruction
- Temperature extremes
- Reproductive emergencies

**Urgent Indicators**:
- Eye emergencies
- Severe pain
- Allergic reactions
- Complete anorexia >24 hours
- Sudden behavioral changes

### Immediate Escalation

If emergency indicators are detected:
- Assessment HALTS immediately
- Emergency veterinary resources provided
- No diagnostic or treatment advice given
- Clear direction to seek professional care

---

## Evidence-Based Approach

### Research-First Philosophy

The skill prioritizes current evidence over cached knowledge:

1. **WebSearch**: Queries authoritative veterinary sources
2. **WebFetch**: Retrieves full content for verification
3. **Evidence Grading**: Assigns tier levels (1-6) to each source
4. **Framework Application**: Uses recognized guidelines
5. **Graceful Degradation**: Falls back to cached knowledge when needed

### Evidence Hierarchy

| Tier | Type | Example |
|------|------|---------|
| Tier 1 | Systematic Review/Meta-Analysis | Cochrane reviews |
| Tier 2 | Randomized Controlled Trial | Clinical trials |
| Tier 3 | Cohort Study | Longitudinal studies |
| Tier 4 | Expert Consensus/Guidelines | AAHA, WSAVA guidelines |
| Tier 5 | Case Reports/Opinion | Individual case reports |
| Tier 6 | Unverified Claims | Unsubstantiated claims |

---

## Output Format

The skill produces a comprehensive report including:

1. **Executive Summary**: Overall grade, top strengths, priority improvements
2. **Scoring Table**: All 6 dimensions with scores and frameworks
3. **Detailed Analysis**: Per-dimension breakdown with citations
4. **Challenge Notes**: Devil's-advocate review results
5. **Prioritized Roadmap**: Actionable recommendations ranked by impact/effort
6. **Implementation Timeline**: When to implement each recommendation
7. **Veterinary Schedule**: When to seek professional care
8. **Sources**: All citations with evidence grades

---

## Knowledge Base

### Self-Improving Knowledge

The skill maintains a growing knowledge base (`SECOND-KNOWLEDGE-BRAIN.md`) that:
- Crawls authoritative veterinary sources weekly
- Scores entries by recency and relevance
- De-duplicates by URL/DOI hash
- Stores entries for offline/degraded mode operation

### Knowledge Refresh Tool

`tools/knowledge_updater.py`:
- Fetches from ArXiv (q-bio.QM categories)
- Crawls authoritative domain sources
- Applies relevance scoring
- Appends new, de-duplicated entries

**Setup**:
```bash
cd tools
pip install -r requirements.txt
python knowledge_updater.py
```

**Scheduled Execution**:
```bash
# Add to crontab for weekly execution
0 2 * * 0 cd /path/to/skill && python tools/knowledge_updater.py
```

---

## Testing

### Test Scenarios

Comprehensive test scenarios are defined in `tests/test-scenarios.md`:

1. **Happy Path**: Healthy adult dog full evaluation
2. **Incomplete Input**: Intake clarification path
3. **Degraded Mode**: Offline fallback operation
4. **Emergency Escalation**: Red flag detection and routing
5. **Challenge Phase**: Score revision through devil's-advocate review
6. **Cross-Species**: Rabbit assessment (non-dog/cat)
7. **Roadmap-Only**: Prioritized recommendations without full analysis

### Running Tests

Tests can be run manually by following each scenario's input data and
validating against expected outputs. Automated test implementation
is planned for future development.

---

## Development Status

| Phase | Status | Description |
|-------|--------|-------------|
| Phase 0 | ✅ Complete | Research & Skill Architecture |
| Phase 1 | ✅ Complete | Core Sub-Skills Implementation |
| Phase 2 | ✅ Complete | Main Harness + Quality Gates |
| Phase 3 | ✅ Complete | Knowledge Pipeline Implementation |
| Phase 4 | ✅ Complete | Testing & Validation Suite |
| Phase 5 | ✅ Complete | Cross-Skill Integration |

**Overall**: 100% Complete, Production-Ready

---

## Cluster Integration

This skill is part of the `lifestyle-personal` cluster and serves as the
reference implementation for cluster-wide patterns:

- **Shared Sub-Skills**: Profile intake, safety screening, scoring, roadmap
- **Standardized Output**: Common report structure across cluster
- **Quality Gates**: Consistent safety and quality standards
- **Evidence Grading**: Shared evidence hierarchy

See `CLUSTER-INTEGRATION.md` for details on cross-skill compatibility.

---

## Contributing

This skill is production-ready and open-source. When contributing:

1. **Maintain Evidence-Based Standards**: All claims must cite authoritative sources
2. **Preserve Safety Gates**: Never bypass emergency screening
3. **Follow Cluster Patterns**: Maintain compatibility with cluster standards
4. **Test Thoroughly**: Use the test scenarios to validate changes
5. **Update Documentation**: Keep all documentation in sync

---

## License

This skill is provided as open-source educational content. It is not a
substitute for professional veterinary care.

---

## Acknowledgments

**Frameworks Authored By**:
- American Animal Hospital Association (AAHA)
- World Small Animal Veterinary Association (WSAVA)
- American Veterinary Medical Association (AVMA)
- ASPCA
- Merck Veterinary Manual
- Five Domains Model (Mellor et al.)

**Tools & Libraries**:
- Claude Code (Anthropic)
- crawl4ai (Web crawling)
- ArXiv API (Academic papers)

---

## Contact & Support

For questions about this skill:
- Review the test scenarios for usage examples
- Check the technical specification (PROJECT-detail.md)
- Consult the cluster integration guide (CLUSTER-INTEGRATION.md)

For veterinary emergencies:
- Contact your local emergency veterinary hospital
- Animal Poison Control: (888) 426-4435 (US/Canada)

---

**Version**: 1.0.0
**Last Updated**: 2026-06-19
**Status**: Production-Ready ✓
