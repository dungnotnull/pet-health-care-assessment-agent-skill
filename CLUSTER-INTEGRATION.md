# Lifestyle & Personal Cluster Integration

**Cluster**: `lifestyle-personal`
**Skill**: `pet-health-care-assessment` (Idea #82)

This document defines how this skill integrates with other skills in the
lifestyle-personal cluster, including shared sub-skills, standardized output
formats, and cross-skill compatibility.

---

## Cluster Context

The `lifestyle-personal` cluster contains skills that help users optimize
various aspects of their personal and family life. Skills in this cluster
share common patterns around assessment, prioritization, and improvement
planning.

### Related Skills in Cluster

| Skill | Idea # | Focus | Shared Components |
|-------|--------|-------|-------------------|
| pet-health-care-assessment | 82 | Pet health evaluation | Intake, Scoring, Roadmap |
| [Future skill: personal-health-assessment] | TBD | Human health optimization | Intake, Scoring, Roadmap |
| [Future skill: home-organization-assessment] | TBD | Living space optimization | Intake, Scoring, Roadmap |
| [Future skill: family-finance-assessment] | TBD | Financial health evaluation | Intake, Scoring, Roadmap |
| [Future skill: personal-development-assessment] | TBD | Growth planning | Intake, Scoring, Roadmap |

---

## Shared Sub-Skills

The following sub-skills are designed for reuse across cluster skills:

### 1. Profile Intake (shared-pattern)

**Purpose**: Collect demographic/contextual information with disclaimers

**Shared Structure**:
- Mandatory disclaimer presentation
- Required field collection
- Data quality scoring
- Missing data handling
- Species/Domain-specific questions

**Skill-Specific Adaptations**:
- Pet health: Species, breed, age, weight, medical history
- Personal health: Age, gender, medical history, lifestyle factors
- Home organization: Space size, occupancy, usage patterns
- Finance: Income, expenses, debts, goals

**Shared Output Format**:
```json
{
  "meta": {
    "disclaimer_acknowledged": true,
    "intake_timestamp": "ISO-8601",
    "domain_category": "string"
  },
  "demographics": { /* domain-specific */ },
  "history": { /* domain-specific */ },
  "current_state": { /* domain-specific */ },
  "concerns": { /* domain-specific */ },
  "data_quality": {
    "completeness_score": 0.0-1.0,
    "missing_critical_fields": [],
    "uncertain_fields": [],
    "flags": []
  }
}
```

### 2. Safety Screener (shared-pattern)

**Purpose**: Screen for emergency/urgent conditions BEFORE any guidance

**Shared Structure**:
- Emergency red flag detection
- Urgent condition detection
- Escalation to professional resources
- Stop-assessment trigger

**Skill-Specific Adaptations**:
- Pet health: Veterinary emergency indicators
- Personal health: Medical emergency indicators
- Home organization: Safety hazards (not applicable in same way)
- Finance: Financial crisis indicators

**Shared Decision Tree**:
```
IF emergency flags:
    RETURN [EMERGENCY_ESCALATION]
    STOP assessment
ELSE IF urgent flags:
    RETURN [URGENT_RECOMMENDATION]
    MAY CONTINUE with caution
ELSE:
    RETURN [CLEAR]
    PROCEED to assessment
```

### 3. Framework Selector & Scoring (shared-pattern)

**Purpose**: Apply domain frameworks to score current state

**Shared Structure**:
- Framework selection based on domain/sub-category
- Multi-dimensional scoring (0-5 scale)
- Evidence-based justifications
- Weighted overall score calculation

**Skill-Specific Adaptations**:
- Pet health: 6 dimensions, AAHA/WSAVA frameworks
- Personal health: N dimensions, clinical guidelines
- Home organization: N dimensions, organization principles
- Finance: N dimensions, financial health metrics

**Shared Scoring Pattern**:
```json
{
  "dimension_scores": {
    "dimension_name": {
      "score": 0.0-5.0,
      "framework": "Framework Name",
      "evidence_grade": "Tier 1-6",
      "justification": "Brief rationale",
      "source": "URL or citation"
    }
  },
  "overall_score": {
    "weighted_mean": 0.0-5.0,
    "grade": "Excellent/Critical/etc.",
    "interpretation": "Description"
  }
}
```

### 4. Improvement Roadmap (shared-pattern)

**Purpose**: Generate prioritized recommendations with impact/effort analysis

**Shared Structure**:
- Challenge phase (devil's-advocate review)
- Impact/Effort prioritization matrix
- Timeline generation
- Resource trigger specification

**Skill-Specific Adaptations**:
- Pet health: Vet visit triggers, medical considerations
- Personal health: Doctor visit triggers, lifestyle changes
- Home organization: Project complexity, space requirements
- Finance: Cost/benefit analysis, time investment

**Shared Roadmap Format**:
```markdown
## Prioritized [Domain] Roadmap

### Priority 1: Quick Wins (High Impact, Low/Medium Effort)
| # | Recommendation | Impact | Effort | Timeline | Resource Trigger |
|---|----------------|--------|--------|----------|------------------|

### Priority 2: Moderate Wins (Medium Impact, Low/Medium Effort)
[Same format]

### Priority 3: Major Projects (High Impact, High Effort)
[Same format]

### Priority 4: Fill-In Items (Low Impact, Any Effort)
[Same format]
```

---

## Standardized Output Formats

### Cluster-Level Report Structure

All cluster skills should produce reports with these sections:

```markdown
# [Domain] Assessment — Evaluation Report

**Profile**: [Key demographics]
**Assessment Date**: [Date]
**Overall Score**: [X.X]/5.0 ([Grade])

---

## ⚠️ Important Disclaimer

## Executive Summary
- Overall Grade
- Top Strengths
- Top Priority Improvements

## Scoring Results
[Table of dimension scores]

## Detailed Analysis by Dimension
[Per-dimension analysis with citations]

## Challenge / Devil's-Advocate Notes
[Counter-arguments considered]

## Prioritized Improvement Roadmap
[Prioritized recommendations table]

## Implementation Timeline
[Timeline by priority]

## [Professional] Visit Schedule
[Professional resource triggers]

## Owner Considerations
[Resource requirements]

## Sources & Evidence Grade
[Citations with evidence tiers]

## Quality Indicators
[Checklist of quality gates passed]
```

---

## Cross-Skill Compatibility

### Shared Quality Gates

All cluster skills should implement these quality gates:

1. **Disclaimer**: Presented and acknowledged before assessment
2. **Safety Screening**: Completed before any guidance
3. **Data Completeness**: Minimum required fields collected
4. **Evidence Citation**: All claims cite sources with evidence grades
5. **Challenge Phase**: Devil's-advocate review completed
6. **Safety Re-verification**: Final check before output
7. **Professional Triggers**: Clear when professional help is needed

### Shared Evidence Hierarchy

All cluster skills use this evidence grading:

| Tier | Type | Description |
|------|------|-------------|
| Tier 1 | Systematic Review/Meta-Analysis | Highest evidence |
| Tier 2 | Randomized Controlled Trial | Experimental |
| Tier 3 | Cohort Study | Observational longitudinal |
| Tier 4 | Expert Consensus/Guidelines | Professional standards |
| Tier 5 | Case Reports/Opinion | Limited evidence |
| Tier 6 | Unverified Claims | Lowest evidence |

### Shared Score Interpretation

All cluster skills use this score scale:

| Score Range | Grade | Interpretation |
|-------------|-------|----------------|
| 4.5-5.0 | Excellent | Optimal across all dimensions |
| 4.0-4.49 | Very Good | High quality with minor gaps |
| 3.5-3.99 | Good | Solid with improvement opportunities |
| 3.0-3.49 | Fair | Adequate with several needs |
| 2.0-2.99 | Poor | Significant gaps needing attention |
| 1.0-1.99 | Serious | Major concerns, urgent attention |
| 0.0-0.99 | Critical | Emergency intervention required |

---

## Cluster-Level Constants

### Impact/Effort Ratings

**Impact** (positive effect if implemented):
- High (H): Significant improvement
- Medium (M): Moderate improvement
- Low (L): Minor improvement

**Effort** (resource requirements):
- High (H): Significant cost/time/behavioral change
- Medium (M): Moderate cost/time/change
- Low (L): Minimal cost/time/change

### Priority Categories

| Priority Score | Impact | Effort | Label |
|----------------|--------|--------|-------|
| 5-6 | High | Low/Med | QUICK WINS (Do First) |
| 4 | High | High | MAJOR PROJECTS (Plan For) |
| 3 | Medium | Low/Med | MODERATE WINS (Do Soon) |
| 2 | Medium | High | CONSIDER (Evaluate ROI) |
| 1 | Low | Low/Med | FILL-IN (When Convenient) |
| 0-1 | Low | High | LOW PRIORITY (Last) |

---

## Future Cluster Skills

When adding new skills to this cluster, ensure:

1. **Reusability**: Use shared sub-skill patterns where applicable
2. **Compatibility**: Output format matches cluster standard
3. **Quality Gates**: Implement all cluster-level quality gates
4. **Evidence Grading**: Use shared evidence hierarchy
5. **Scoring Consistency**: Score scales align with cluster standards

### Recommended New Skills

1. **Personal Health Assessment**
   - Dimensions: Nutrition, Exercise, Preventive Care, Mental Health, Sleep, Stress Management
   - Frameworks: WHO guidelines, CDC recommendations, clinical guidelines
   - Similar structure to pet health but for human wellness

2. **Home Organization Assessment**
   - Dimensions: Space Efficiency, Organization Systems, Safety, Maintenance, Accessibility
   - Frameworks: Professional organizing principles, minimal design principles
   - Similar scoring/roadmap approach

3. **Family Finance Assessment**
   - Dimensions: Budget Management, Debt Handling, Savings, Investment, Emergency Preparedness
   - Frameworks: Financial planning standards, CFP guidelines
   - Similar priority/effort matrix

4. **Personal Development Assessment**
   - Dimensions: Learning Goals, Career Development, Relationships, Skills, Purpose
   - Frameworks: Developmental psychology, coaching frameworks
   - Similar improvement roadmap approach

---

## Implementation Notes

### For This Skill (Pet Health)

This skill is the FIRST implementation in the cluster and sets the pattern
for subsequent skills. As such, it represents the reference implementation
for cluster patterns.

### For Future Skills

When implementing cluster skills:
1. Reference this skill's structure as a template
2. Adapt domain-specific content while maintaining structure
3. Ensure all shared components are truly shared (not duplicated)
4. Update this document with any new shared patterns discovered

---

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2026-06-19 | 1.0 | Initial cluster integration document |
| | | Reference implementation established |

---

**Document Owner**: pet-health-care-assessment skill (idea #82)
**Cluster**: lifestyle-personal
**Status**: Active - Reference Implementation
