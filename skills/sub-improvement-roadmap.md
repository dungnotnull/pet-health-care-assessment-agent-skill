---
name: sub-improvement-roadmap
description: (pet-health-care-assessment) Build a preventive-care, nutrition and vaccination plan with vet-visit triggers, including challenge phase and impact/effort prioritization.
---

# Sub-skill: Improvement Roadmap & Challenge Phase

## Purpose
Generate a prioritized improvement roadmap based on the scoring results, run a devil's-advocate challenge phase to validate findings, and produce actionable recommendations with impact/effort ratings. Includes vet-visit triggers and timeline guidance.

## When the Harness Calls This
Stage matching `sub-improvement-roadmap` in the `pet-health-care-assessment` main workflow. Runs AFTER:
1. Profile intake (demographics collected)
2. Safety screener (cleared)
3. Research phase (evidence gathered)
4. Framework selector (dimensions scored)

## Challenge Phase (Devil's-Advocate Review)

BEFORE generating recommendations, challenge the scoring results:

### Required Challenge Questions

**Challenge 1: Alternative Interpretation**
"Could the observed data points be explained by a different cause or interpretation than the one I've assigned?"
- Identify the most plausible alternative explanation for low scores
- Assess whether this changes the priority

**Challenge 2: Selection Bias**
"Am I giving too much weight to certain information because it was more prominently reported?"
- Check for overemphasis on owner-reported concerns vs. objective findings
- Verify that silent areas (not mentioned) weren't assumed to be good

**Challenge 3: Framework Mismatch**
"Am I applying frameworks that may not be appropriate for this specific pet's situation?"
- Consider breed, individual health status, owner circumstances
- Assess whether guideline modifications are needed

**Challenge 4: Resource Constraints**
"Am I making recommendations without considering the owner's actual resources and constraints?"
- Financial limitations
- Time constraints
- Geographic access to veterinary care
- Owner's physical capabilities

**Challenge 5: Risk-Benefit Balance**
"For each recommendation, does the potential benefit outweigh the stress/cost/risk to the pet?"
- Consider individual temperament
- Consider medical conditions that might make some interventions risky
- Consider quality of life impact

### Challenge Phase Output Format
```markdown
## Challenge / Devil's-Advocate Notes

### Counter-Argument 1: [Alternative interpretation considered]
**Challenge**: [Description of alternative explanation]
**Resolution**: [Why original scoring stands or how it was revised]

### Counter-Argument 2: [Potential bias identified]
**Challenge**: [Description of bias concern]
**Resolution**: [How bias was addressed]

### Counter-Argument 3: [Framework appropriateness questioned]
**Challenge**: [Question about framework fit]
**Resolution**: [Adaptation made or validation of fit]

### Counter-Argument 4: [Resource constraint consideration]
**Challenge**: [Owner limitation factor]
**Resolution**: [Recommendation adjusted or acknowledged]

### Counter-Argument 5: [Risk-benefit analysis]
**Challenge**: [Potential downside of recommendation]
**Resolution**: [How recommendation was modified]

**Scoring Revisions Based on Challenge Phase**:
- [Any dimension scores that changed]
- [Rationale for revision]
```

---

## Prioritization Framework

### Impact/Effort Matrix

Each recommendation receives two ratings:

**Impact** (Positive effect on health/welfare if implemented):
- **High (H)**: Significant improvement in quality of life or prevention of serious disease
- **Medium (M)**: Moderate improvement or preventive benefit
- **Low (L)**: Minor improvement or incremental benefit

**Effort** (Resource requirements to implement):
- **High (H)**: Significant financial cost, time investment, or behavioral change required
- **Medium (M)**: Moderate cost/time, reasonable behavioral change
- **Low (L)**: Minimal cost/time, simple change

### Priority Ranking Formula

Priority Score = (Impact Value) - (Effort Value)

Where:
- High Impact = 3, Medium = 2, Low = 1
- High Effort = 3, Medium = 2, Low = 1

**Priority Categories**:
| Priority Score | Impact | Effort | Category |
|----------------|--------|--------|----------|
| 5-6 | High | Low/Med | QUICK WINS (Do First) |
| 4 | High | High | MAJOR PROJECTS (Plan for) |
| 3 | Medium | Low/Med | MODERATE WINS (Do Soon) |
| 2 | Medium | High | CONSIDER (Evaluate ROI) |
| 1 | Low | Low/Med | FILL-IN (When convenient) |
| 0-1 | Low | High | LOW PRIORITY (Last) |

---

## Recommendation Templates by Dimension

### Dimension 1: Nutrition & Body Condition

**Score 5.0**:
- Continue current excellent nutrition
- Maintain current feeding practices
- Monitor weight monthly

**Score 3.0-4.5**:
| Recommendation | Impact | Effort | Priority | Timeline |
|----------------|--------|--------|----------|----------|
| Transition to life-stage appropriate diet meeting WSAVA criteria | High | Medium | Moderate | 2-4 weeks |
| Implement measured portions (use kitchen scale or measuring cup) | High | Low | Quick Win | Immediate |
| Reduce treats to <10% of daily calories | Medium | Medium | Moderate | 1-2 weeks |
| Add appropriate fresh vegetables (species-specific) | Low | Low | Fill-In | When convenient |

**Score <3.0**:
| Recommendation | Impact | Effort | Priority | Timeline | Vet Trigger |
|----------------|--------|--------|----------|----------|-------------|
| Schedule veterinary nutrition consultation | High | Medium | Quick Win | Within 2 weeks | Recommended |
| Transition to therapeutic diet if prescribed | High | Medium | Moderate | As directed | Required if prescribed |
| Address body condition (weight loss/gain plan) | High | High | Major | 3-6 months | Required |

### Dimension 2: Preventive Care & Vaccination

**Score 5.0**:
- Maintain current preventive schedule
- Annual wellness exam already scheduled

**Score 3.0-4.5**:
| Recommendation | Impact | Effort | Priority | Timeline | Vet Trigger |
|----------------|--------|--------|----------|----------|-------------|
| Schedule wellness exam if >14 months since last | High | Medium | Quick Win | Within 4 weeks | Recommended |
| Update overdue core vaccinations | High | Medium | Moderate | Within 8 weeks | Required for boarding/many services |
| Establish year-round parasite prevention | High | Low | Quick Win | Immediate | Recommended |
| Start dental home care (brushing or dental treats) | Medium | Medium | Moderate | 2-4 weeks | Recommended |

**Score <3.0**:
| Recommendation | Impact | Effort | Priority | Timeline | Vet Trigger |
|----------------|--------|--------|----------|----------|-------------|
| Establish veterinary care relationship (new patient exam) | High | High | Major | Within 2 weeks | Urgent |
| Complete core vaccination series | High | Medium | Quick Win | As per schedule | Required |
- Begin comprehensive parasite prevention protocol | High | Low | Quick Win | Immediate | Recommended |
| Baseline bloodwork and health screening | High | Medium | Moderate | At wellness visit | Recommended |
| Dental cleaning/prophylaxis if indicated | High | High | Major | Within 3 months | Recommended if periodontal disease |

### Dimension 3: Symptom/Red-Flag Screening

**Score 5.0**:
- Continue monitoring health at home
- No concerns requiring action

**Score 3.0-4.5**:
| Recommendation | Impact | Effort | Priority | Timeline | Vet Trigger |
|----------------|--------|--------|----------|----------|-------------|
| Schedule veterinary evaluation for noted symptom(s) | High | Medium | Moderate | Within 2 weeks | Recommended |
| Begin symptom diary to track changes | Medium | Low | Quick Win | Immediate | Helpful for diagnosis |
| Home monitoring of [specific parameter] | Medium | Low | Quick Win | Daily | Helpful |

**Score <3.0**:
| Recommendation | Impact | Effort | Priority | Timeline | Vet Trigger |
|----------------|--------|--------|----------|----------|-------------|
| URGENT: Veterinary evaluation for concerning symptoms | High | Medium | Quick Win | Within 48 hours | Urgent |
| Prepare symptom history for veterinarian | High | Low | Quick Win | Before appointment | Helpful |
| Consider diagnostics (bloodwork, imaging) as recommended | High | High | Major | As directed | Recommended |

### Dimension 4: Behavior & Enrichment

**Score 5.0**:
- Continue current enrichment practices
- Maintain behavioral health

**Score 3.0-4.5**:
| Recommendation | Impact | Effort | Priority | Timeline |
|----------------|--------|--------|----------|----------|
| Add daily mental enrichment (puzzle toys, training) | Medium | Low | Quick Win | Immediate |
| Increase exercise by [species-specific amount] | Medium | Medium | Moderate | 1-2 weeks |
- Address [specific behavioral concern] with positive reinforcement | High | Medium | Moderate | 2-4 weeks |
| Provide species-appropriate social opportunities | Medium | Variable | Variable | As appropriate |

**Score <3.0**:
| Recommendation | Impact | Effort | Priority | Timeline | Vet Trigger |
|----------------|--------|--------|----------|----------|-------------|
| Consult with veterinarian about behavioral concerns | High | Medium | Quick Win | Within 4 weeks | Recommended |
| Consider referral to veterinary behaviorist | High | High | Major | Within 8 weeks | Recommended if severe |
| Implement comprehensive behavior modification plan | High | High | Major | 8-12 weeks | Recommended with professional guidance |
- Environmental modification to reduce stress | Medium | Medium | Moderate | 2-4 weeks | Recommended |

### Dimension 5: Environment & Husbandry

**Score 5.0**:
- Maintain current excellent environment

**Score 3.0-4.5**:
| Recommendation | Impact | Effort | Priority | Timeline |
|----------------|--------|--------|----------|----------|
| Optimize [specific environmental parameter] | Medium | Low | Quick Win | Immediate |
| Improve cleaning schedule for housing/litter box | Medium | Low | Quick Win | Immediate |
| Add environmental enrichment (hiding spots, vertical space) | Medium | Medium | Moderate | 1-2 weeks |
- Ensure clean water always available | High | Low | Quick Win | Immediate |

**Score <3.0**:
| Recommendation | Impact | Effort | Priority | Timeline |
|----------------|--------|--------|----------|----------|
| URGENT: Address [critical environmental deficiency] | High | High | Major | Immediate |
- Upgrade housing to appropriate size/specifications | High | High | Major | 2-4 weeks |
| Establish appropriate temperature/humidity control | High | High | Major | 1-2 weeks |
| Implement deep cleaning protocol | High | Medium | Moderate | Immediate |

### Dimension 6: Life-Stage Appropriateness

**Score 5.0**:
- Continue life-stage appropriate care

**Score 3.0-4.5**:
| Recommendation | Impact | Effort | Priority | Timeline | Vet Trigger |
|----------------|--------|--------|----------|----------|-------------|
| Transition to life-stage appropriate diet | High | Low | Quick Win | 1-2 weeks | Recommended |
| Adjust exercise to match life-stage needs | Medium | Medium | Moderate | 2-4 weeks | Recommended |
| Schedule age-appropriate health screenings | High | Medium | Moderate | At next wellness visit | Recommended |
| Consider life-stage specific preventive measures | Medium | Variable | Variable | As appropriate | Recommended |

**Score <3.0**:
| Recommendation | Impact | Effort | Priority | Timeline | Vet Trigger |
|----------------|--------|--------|----------|----------|-------------|
| Comprehensive life-stage care consultation | High | Medium | Quick Win | Within 4 weeks | Recommended |
- Implement complete life-stage appropriate care plan | High | High | Major | 4-8 weeks | Recommended |
| Address age-specific health monitoring | High | Medium | Moderate | As directed | Required for seniors/geriatrics |

---

## Vet Visit Triggers

Define when veterinary consultation is RECOMMENDED vs REQUIRED vs URGENT:

### Recommended
- Annual wellness exam (or semi-annual for seniors)
- Weight management plan initiation
- Behavioral concerns
- Preventive care optimization

### Required
- Vaccination updates
- Prescribed therapeutic diet
- Dental care requiring professional cleaning
- Health screening as per age/life stage
- Symptom evaluation

### Urgent (within 48-72 hours)
- New concerning symptoms
- Acute behavioral changes
- Minor injuries
- Sudden changes in appetite, elimination, or activity

### Emergency (IMMEDIATE)
- Any red flag symptoms (should have been caught by safety screener)
- Difficulty breathing
- Collapse/loss of consciousness
- Uncontrolled bleeding
- Suspected poisoning
- Trauma
- Urinary obstruction
- GDV/bloat signs

---

## Output Format

```markdown
## Prioritized Improvement Roadmap

### Priority 1: Quick Wins (High Impact, Low/Medium Effort)
| # | Recommendation | Impact | Effort | Framework Basis | Timeline | Vet Visit |
|---|----------------|--------|--------|----------------|----------|-----------|
| 1 | [Recommendation] | H | L/M | [Framework] | [Timeline] | [Trigger] |

### Priority 2: Moderate Wins (Medium Impact, Low/Medium Effort)
| # | Recommendation | Impact | Effort | Framework Basis | Timeline | Vet Visit |
|---|----------------|--------|--------|----------------|----------|-----------|
| [Similar format] |

### Priority 3: Major Projects (High Impact, High Effort - Plan For)
| # | Recommendation | Impact | Effort | Framework Basis | Timeline | Vet Visit |
|---|----------------|--------|--------|----------------|----------|-----------|
| [Similar format] |

### Priority 4: Fill-In Items (Low Impact, When Convenient)
| # | Recommendation | Impact | Effort | Framework Basis | Timeline | Vet Visit |
|---|----------------|--------|--------|----------------|----------|-----------|
| [Similar format] |

## Implementation Timeline Summary
- **Immediate (Start Today)**: [List]
- **1-2 Weeks**: [List]
- **1 Month**: [List]
- **2-3 Months**: [List]
- **3-6 Months**: [List]

## Veterinary Visit Schedule
- **Next wellness exam due**: [Date or "within X months"]
- **Priority vet visits needed**: [List with urgency]

## Owner Considerations
- **Financial prioritization**: [Guidance on budgeting for recommendations]
- **Time requirements**: [Estimate of weekly time commitment]
- **Behavioral changes**: [Note any significant changes required]

## Success Metrics
How to tell if improvements are working:
- [Dimension-specific success indicators]
- [Timeline for reassessment]
- [When to schedule follow-up evaluation]
```

---

## Quality Gates

Before passing to final synthesis:
- [ ] Challenge phase completed with ≥5 counter-arguments
- [ ] All low-scoring dimensions (≤3.0) have prioritized recommendations
- [ ] Each recommendation has impact/effort rating
- [ ] Recommendations ranked by priority score
- [ ] Vet visit triggers clearly specified
- [ ] Timeline provided for each recommendation
- [ ] Owner resource constraints considered
- [ ] Framework basis cited for each recommendation

## Special Considerations

### For Owners with Financial Constraints
Prioritize:
1. Preventive care (vaccines, parasite prevention)
2. Nutrition optimization (often cost-neutral)
3. Environmental improvements
4. Deferred: Major projects that can be planned and saved for

### For Time-Constrained Owners
Prioritize:
1. Quick wins that require minimal time
2. Habit-based changes (e.g., feeding measured portions)
3. Automatic systems (e.g., monthly parasite prevention delivery)
4. Deferred: Time-intensive behavioral programs

### For Multiple-Pet Households
Address:
- Individual recommendations per pet
- Shared environmental improvements
- Cross-contamination risks (infectious disease)
- Resource allocation strategies

### For Senior/ Geriatric Pets
Additional focus on:
- Quality of life metrics
- Comfort and mobility
- Cognitive health
- Pain management
- End-of-life planning when appropriate

### For Pediatric/Puppies/Kittens
Additional focus on:
- Socialization window
- Preventive series completion
- Behavior foundation
- Spay/neuter timing
- Growth monitoring
