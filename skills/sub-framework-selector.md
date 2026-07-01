---
name: sub-framework-selector
description: (pet-health-care-assessment) Apply the species/life-stage AAHA/WSAVA guideline set and score across 6 dimensions.
---

# Sub-skill: Framework Selector & Scoring Engine

## Purpose
Apply species-appropriate veterinary frameworks (AAHA life-stage care guidelines, WSAVA nutrition & body-condition scoring, Vaccination core/non-core schedules, Five Domains welfare model) to evaluate the pet's current care across 6 standardized dimensions. Generate numerical scores with evidence-based justifications.

## When the Harness Calls This
Stage matching `sub-framework-selector` in the `pet-health-care-assessment` main workflow. Runs AFTER:
1. Profile intake (demographics and history collected)
2. Safety screener (cleared for continued assessment)
3. Research phase (evidence gathered)

## Scoring Framework Overview

### The Six Evaluation Dimensions
Each dimension receives a score from 0-5 with half-point precision:

| Dimension | Weight | Framework(s) Applied |
|-----------|--------|---------------------|
| 1. Nutrition & Body Condition | 1.0 | WSAVA Nutrition Guidelines, BCS (Body Condition Score) |
| 2. Preventive Care & Vaccination | 1.0 | AAHA/WSAVA Vaccination Guidelines, AAHA Life-Stage Care |
| 3. Symptom/Red-Flag Screening | 1.5 | Triage Red-Flag Protocols, AAHA Health Screening |
| 4. Behavior & Enrichment | 0.75 | Five Domains Model (Behavior domain), AAHA Behavior Guidelines |
| 5. Environment & Husbandry | 0.75 | Five Domains Model (Environment domain), Species-Specific Standards |
| 6. Life-Stage Appropriateness | 1.0 | AAHA Life-Stage Guidelines (Puppy/Kitten/Adult/Senior/Geriatric) |

**Overall Score** = Weighted mean of dimension scores (weights sum to 5.0)

---

## Scoring Rubrics by Dimension

### Dimension 1: Nutrition & Body Condition (0-5)

**Framework**: WSAVA Nutrition Guidelines + Body Condition Scoring (BCS)

| Score | Criteria | Evidence Indicators |
|-------|----------|---------------------|
| 5.0 | Optimal nutrition; ideal BCS; life-stage appropriate | - Commercial diet meeting WSAVA criteria (AAFCO/FCO approved)<br>- BCS 4-5/9 (dogs) or 5/9 (cats)<br>- No inappropriate supplements<br>- Controlled portions for weight maintenance |
| 4.5 | Excellent nutrition; minor room for improvement | - WSAVA-compliant diet<br>- BCS slightly above/below ideal (6/9 or 3/9)<br>- Appropriate treats (<10% calories)<br>- Life-stage diet being used |
| 4.0 | Good nutrition; one notable concern | - Generally appropriate diet<br>- BCS borderline overweight/underweight<br>- Some supplements lacking evidence<br>- Portion control could improve |
| 3.0 | Adequate nutrition; multiple concerns | - Diet not life-stage appropriate<br>- BCS indicates over/under condition (7+/9 or 2-/9)<br>- Excessive treats or table food<br>- Missing preventive nutrients |
| 2.0 | Poor nutrition; significant gaps | - Inappropriate diet for species (e.g., grain-free without indication)<br>- BCS concerning (8+/9 or 1-2/9)<br>- Raw diet without safety protocols<br>- Major nutritional imbalances |
| 1.0 | Dangerous nutrition; immediate risks | - Known toxic foods being fed<br>- Severe obesity (9/9) or emaciation<br>- Nutritional deficiencies causing clinical signs<br>- Home-prepared diet without veterinary formulation |
| 0.0 | Emergency nutrition; life-threatening | - Diet causing acute illness<br>- Obstruction risk from feeding practices<br>- Severe malnutrition evident |

**Scoring Algorithm**:
```
Base Score: Evaluate diet quality (5=WSAVA-compliant, 3=adequate, 1=poor)
BCS Adjustment: Ideal BCS = +0; ±1 point = -0.5; ±2 points = -1; ±3+ = -1.5
Life-Stage Factor: Appropriate = +0; Inappropriate = -1
Treats/Supplements Factor: Controlled = +0; Excessive = -0.5; Dangerous = -1

Final Score = Base + BCS Adjustment + Life-Stage Factor + Treats Factor
```

### Dimension 2: Preventive Care & Vaccination (0-5)

**Framework**: AAHA/WSAVA Vaccination Guidelines + AAHA Life-Stage Preventive Care

| Score | Criteria | Evidence Indicators |
|-------|----------|---------------------|
| 5.0 | Complete preventive care; optimal schedule | - Core vaccines current per AAHA/WSAVA<br>- Annual wellness exam completed<br>- Parasite prevention consistent (yearly heartworm, flea/tick)<br>- Dental care plan active<br>- Screenings appropriate for life stage |
| 4.5 | Excellent preventive care; minor gaps | - Core vaccines current<br>- Wellness exam within 14 months<br>- Parasite prevention mostly consistent<br>- Some preventive care could be optimized |
| 4.0 | Good preventive care; one notable gap | - Core vaccines current<br>- Wellness exam within 18 months<br>- Parasite prevention intermittent<br>- Missing one preventive element (e.g., dental) |
| 3.0 | Adequate preventive care; multiple gaps | - Core vaccines overdue or incomplete<br>- Wellness exam >2 years ago<br>- Parasite prevention inconsistent<br>- Missing several preventive elements |
| 2.0 | Poor preventive care; significant gaps | - Core vaccines significantly overdue<br>- No regular wellness care<br>- No consistent parasite prevention<br>- No preventive screenings |
| 1.0 | Minimal preventive care; serious risks | - No vaccination history<br>- No veterinary care established<br>- No parasite prevention<br>- High-risk lifestyle without protection |
| 0.0 | No preventive care; immediate risks | - Unknown vaccination status in high-risk situation<br>- No veterinary access in emergency<br>- Zoonotic disease risk present |

**Core Vaccines by Species**:
- **Dogs**: Rabies (required by law), DHPP (Distemper, Hepatitis/Adenovirus, Parvovirus, Parainfluenza)
- **Cats**: Rabies, FVRCP (Feline Viral Rhinotracheitis, Calicivirus, Panleukopenia)

**Non-Core Vaccines** (lifestyle-dependent):
- **Dogs**: Leptospirosis, Lyme, Bordetella, Canine Influenza
- **Cats**: Feline Leukemia (FeLV) for outdoor/exposed cats

**Parasite Prevention Requirements**:
- Heartworm: Year-round prevention in endemic areas
- Fleas/Ticks: Monthly prevention or as needed based on exposure
- Intestinal parasites: Regular deworming per life stage

### Dimension 3: Symptom/Red-Flag Screening (0-5)

**Framework**: Triage Red-Flag Protocols + AAHA Health Screening Guidelines

| Score | Criteria | Evidence Indicators |
|-------|----------|---------------------|
| 5.0 | No concerning symptoms; excellent health | - No red-flag symptoms present<br>- No owner-reported health concerns<br>- Normal activity, appetite, behavior<br>- No undiagnosed changes |
| 4.5 | Very healthy; minor non-urgent symptoms | - 1-2 minor symptoms (e.g., occasional cough)<br>- Owner concerns are preventive/not acute<br>- No changes in normal patterns |
| 4.0 | Healthy; manageable symptoms noted | - Minor symptoms present (e.g., mild tartar, occasional vomiting)<br>- Symptoms not affecting quality of life<br>- No progressive signs |
| 3.0 | Fair health; symptoms warrant investigation | - Multiple symptoms or one moderate symptom<br>- Symptoms affecting some functions<br>- Changes in normal patterns present<br>- Needs veterinary evaluation soon |
| 2.0 | Poor health status; symptoms concerning | - Multiple moderate or one severe symptom<br>- Symptoms significantly affecting quality of life<br>- Clear abnormalities present<br>- Urgent evaluation needed |
| 1.0 | Serious health concerns; significant symptoms | - Severe or progressive symptoms<br>- Multiple concerning signs<br>- Clear decline from baseline<br>- Immediate/priority evaluation needed |
| 0.0 | Emergency; critical symptoms present | - SHOULD HAVE BEEN CAUGHT BY SAFETY SCREENER<br>- Life-threatening symptoms<br>- This score indicates safety screener failed |

**Symptom Categories to Evaluate**:

**System-Specific Symptom Review**:
1. **General**: Lethargy, weakness, fever, weight changes
2. **Respiratory**: Coughing, sneezing, difficulty breathing
3. **Gastrointestinal**: Vomiting, diarrhea, appetite changes, constipation
4. **Urinary**: Changes in urination, accidents, blood
5. **Skin/Ears**: Itching, odor, discharge, wounds
6. **Musculoskeletal**: Limping, stiffness, difficulty rising
7. **Neurological**: Seizures, balance issues, behavior changes
8. **Eyes**: Discharge, redness, vision changes
9. **Behavior**: Anxiety, aggression, confusion, changes

### Dimension 4: Behavior & Enrichment (0-5)

**Framework**: Five Domains Model (Behavior Domain) + AAHA Behavior Guidelines

| Score | Criteria | Evidence Indicators |
|-------|----------|---------------------|
| 5.0 | Excellent behavioral health; optimal enrichment | - Species-typical behaviors expressed<br>- Mental enrichment provided daily<br>- No behavioral concerns<br>- Positive reinforcement training used<br>- Social needs met (if applicable) |
| 4.5 | Very good behavioral health; minor improvements possible | - Mostly species-typical behaviors<br>- Regular enrichment provided<br>- 1 minor behavioral concern (e.g., mild separation anxiety)<br>- Training in place |
| 4.0 | Good behavioral health; one moderate concern | - Most species-typical behaviors present<br>- Enrichment provided but could be more frequent<br>- One moderate behavioral issue present<br>- Training inconsistent |
| 3.0 | Adequate behavioral health; multiple concerns | - Some species-typical behaviors restricted<br>- Enrichment inconsistent<br>- 2-3 behavioral concerns<br>- Training methods unclear |
| 2.0 | Poor behavioral health; significant concerns | - Multiple behavioral restrictions<br>- Minimal enrichment<br>- Multiple concerning behaviors<br>- Training gaps evident |
| 1.0 | Serious behavioral welfare concerns | - Major behavioral problems affecting safety/welfare<br>- No enrichment provided<br>- Behavioral interventions needed<br>- Quality of life significantly impacted |
| 0.0 | Severe behavioral crisis | - Dangerous behaviors present<br>- Complete lack of behavioral support<br>- Emergency behavioral intervention required |

**Species-Specific Behavioral Needs**:

**Dogs**:
- Social interaction (species-appropriate)
- Daily exercise (breed-appropriate duration)
- Mental stimulation (training, puzzle toys)
- Species-typical behaviors (sniffing, chewing, playing)

**Cats**:
- Environmental enrichment (vertical space, hiding spots)
- Hunting/play simulation
- Litter box maintenance (clean, appropriate number)
- Scratching outlets

**Rabbits**:
- Space to hop and run
- Foraging opportunities
- Social companionship (rabbit or human)
- Hide boxes

**Birds**:
- Flight opportunities (if safe)
- Foraging toys
- Social interaction
- Species-typical vocalization opportunities

**Reptiles**:
- Temperature gradients for thermoregulation
- Hiding/shedding areas
- Species-appropriate substrate

### Dimension 5: Environment & Husbandry (0-5)

**Framework**: Five Domains Model (Environment Domain) + Species-Specific Husbandry Standards

| Score | Criteria | Evidence Indicators |
|-------|----------|---------------------|
| 5.0 | Optimal environment; species-appropriate husbandry | - Temperature, humidity, lighting appropriate for species<br>- Clean, safe housing<br>- Appropriate enclosure size<br>- Clean water always available<br>- Air quality excellent |
| 4.5 | Excellent environment; minor improvements possible | - Environmental parameters mostly appropriate<br>- Housing adequate<br>- One element could be optimized (e.g., more space) |
| 4.0 | Good environment; one notable concern | - Generally appropriate environment<br>- One environmental parameter suboptimal<br>- Housing adequate but could improve<br>- Water available |
| 3.0 | Adequate environment; multiple concerns | - Several environmental parameters suboptimal<br>- Housing size marginal for species<br>- Some environmental stressors present<br>- Water access inconsistent |
| 2.0 | Poor environment; significant husbandry gaps | - Inappropriate temperature/humidity/lighting<br>- Inadequate housing size/conditions<br>- Environmental stressors clearly present<br>- Cleanliness or safety concerns |
| 1.0 | Serious environmental welfare concerns | - Severely inappropriate environment<br>- Housing inadequate for species<br>- Multiple environmental stressors<br>- Clear welfare compromise |
| 0.0 | Dangerous environment; immediate welfare crisis | - Life-threatening environmental conditions<br>- No appropriate housing<br.- Environmental hazards present<br>- Immediate intervention required |

**Species-Specific Environmental Standards**:

**Dogs**:
- Shelter from extreme weather
- Safe confinement when unsupervised
- Clean, dry bedding area
- Protection from hazards

**Cats**:
- Indoor environment strongly recommended
- Litter boxes: 1 per cat + 1, scooped daily
- Vertical space (cat trees, shelves)
- Window access or environmental enrichment

**Rabbits**:
- Indoor housing or safe outdoor hutch with temperature control
- Space to hop (minimum 4x2x2 feet for small breed)
- Hide boxes for security
- Regular cleaning to prevent ammonia buildup

**Birds**:
- Cage size allows wing stretching and movement
- Placement away from drafts and kitchens
- Natural light cycle exposure
- Safe toys and perches

**Reptiles**:
- Species-specific temperature gradient
- UVB lighting for diurnal species
- Appropriate humidity levels
- Secure enclosure

### Dimension 6: Life-Stage Appropriateness (0-5)

**Framework**: AAHA Life-Stage Care Guidelines (Puppy/Kitten, Adult, Senior, Geriatric)

| Score | Criteria | Evidence Indicators |
|-------|----------|---------------------|
| 5.0 | Complete life-stage appropriate care | - All age-appropriate preventive measures in place<br>- Diet matches life stage<br>- Health screenings appropriate for age<br>- Exercise/activity level age-appropriate<br>- No preventable age-related risks |
| 4.5 | Excellent life-stage care; minor gaps | - Most age-appropriate care present<br>- One minor element could be optimized<br>- Diet appropriate for life stage |
| 4.0 | Good life-stage care; one notable gap | - Generally age-appropriate<br>- One element not matched to life stage<br>- Some preventive care could improve |
| 3.0 | Adequate life-stage care; multiple gaps | - Some care not matched to life stage<br>- Several elements not optimized for age<br>- Preventive care incomplete for age |
| 2.0 | Poor life-stage alignment; significant gaps | - Care not aligned with life stage needs<br>- Missing key age-appropriate elements<br>- Preventive care not age-appropriate |
| 1.0 | Serious life-stage mismatches | - Major elements inappropriate for life stage<br>- Potential harm from inappropriate care<br>- Missing essential age-specific care |
| 0.0 | Dangerous life-stage mismatch | - Care actively harmful to life stage<br>- Critical age-specific needs completely unmet |

**Life-Stage Definitions**:

**Pediatric (Puppy/Kitten/Juvenile)**: <1 year (small breeds), <18 months (large breeds)
- Vaccination series completion
- Spay/neuter timing
- Socialization period
- Growth-phase nutrition
- Parasite prevention

**Adult**: 1-7 years (dogs), 1-10 years (cats)
- Annual wellness exams
- Maintenance nutrition
- Dental care
- Exercise and weight management
- Behavior maintenance

**Senior**: 7-11 years (dogs), 10-14 years (cats)
- Biannual wellness exams
- Senior nutrition
- Screening for age-related conditions
- Comfort and mobility support
- Cognitive health monitoring

**Geriatric**: 11+ years (dogs), 14+ years (cats)
- Enhanced monitoring for quality of life
- Pain management
- Mobility support
- Cognitive dysfunction screening
- End-of-life planning considerations

---

## Overall Scoring Algorithm

### Weighted Score Calculation
```
Overall Score = (
  (Nutrition × 1.0) +
  (Preventive × 1.0) +
  (Symptom × 1.5) +
  (Behavior × 0.75) +
  (Environment × 0.75) +
  (LifeStage × 1.0)
) / 5.0
```

### Score Interpretation
| Overall Score | Grade | Interpretation |
|---------------|-------|----------------|
| 4.5-5.0 | Excellent | Optimal care across all dimensions |
| 4.0-4.49 | Very Good | High-quality care with minor improvement areas |
| 3.5-3.99 | Good | Solid care with some improvement opportunities |
| 3.0-3.49 | Fair | Adequate care with several improvement needs |
| 2.0-2.99 | Poor | Significant gaps requiring attention |
| 1.0-1.99 | Serious | Major concerns needing urgent attention |
| 0.0-0.99 | Critical | Emergency intervention required |

---

## Evidence Requirement Per Dimension

For each dimension score, MUST provide:
1. **Framework Citation**: Specific guideline applied (e.g., "AAHA 2023 Canine Life-Stage Guidelines")
2. **Evidence Grade**: Tier level (1-6) per evidence hierarchy
3. **Justification**: 1-2 sentences explaining the score
4. **Source Link**: URL or reference to authoritative source

### Citation Format
```
Dimension: [Name]
Score: [X.X]/5
Framework: [Specific guideline name]
Evidence Grade: [Tier 1-6]
Justification: [Brief rationale]
Source: [URL or reference]
```

---

## Framework Selection Logic

### Species-Specific Framework Application

**For Dogs**:
- AAHA 2023 Canine Life-Stage Care Guidelines
- WSAVA 2021 Nutrition Guidelines
- AAHA/WSAVA 2022 Canine Vaccination Guidelines
- Five Domains Model (Canine adaptation)

**For Cats**:
- AAHA 2023 Feline Life-Stage Care Guidelines
- AAFP/WSAVA Nutrition Guidelines
- AAHA/WSAVA 2022 Feline Vaccination Guidelines
- Five Domains Model (Feline adaptation)

**For Rabbits**:
- RCVS/BSAVA Rabbit Welfare Guidelines
- House Rabbit Society Care Guidelines
- Five Domains Model (Lagomorph adaptation)

**For Birds**:
- AAav (Association of Avian Veterinarians) Guidelines
- Five Domains Model (Avian adaptation)

**For Reptiles**:
- ARV (Association of Reptile Veterinarians) Guidelines
- Five Domains Model (Reptile adaptation)

---

## Quality Gates

Before passing scores to the next stage:
- [ ] All 6 dimensions scored with numerical value
- [ ] Each dimension has explicit framework citation
- [ ] Evidence grade assigned per dimension
- [ ] Justification provided for each score
- [ ] Overall weighted score calculated
- [ ] Score interpretation determined
- [ ] No dimension scored without evidence basis

## Output Format

```json
{
  "dimension_scores": {
    "nutrition_body_condition": {
      "score": 4.5,
      "framework": "WSAVA 2021 Nutrition Guidelines",
      "evidence_grade": "Tier 4",
      "justification": "Commercial diet meets WSAVA criteria, BCS 5/9 ideal",
      "source": "URL or citation"
    },
    "preventive_care_vaccination": {
      "score": 4.0,
      "framework": "AAHA 2023 Canine Life-Stage Guidelines",
      "evidence_grade": "Tier 4",
      "justification": "Core vaccines current, wellness exam within 14 months",
      "source": "URL or citation"
    },
    "symptom_red_flag": {
      "score": 5.0,
      "framework": "AAHA Health Screening Guidelines",
      "evidence_grade": "Tier 5",
      "justification": "No concerning symptoms, excellent health status",
      "source": "URL or citation"
    },
    "behavior_enrichment": {
      "score": 4.5,
      "framework": "Five Domains Model - Behavior Domain",
      "evidence_grade": "Tier 4",
      "justification": "Species-typical behaviors expressed, daily enrichment",
      "source": "URL or citation"
    },
    "environment_husbandry": {
      "score": 4.0,
      "framework": "Five Domains Model - Environment Domain",
      "evidence_grade": "Tier 4",
      "justification": "Safe housing, clean environment, water always available",
      "source": "URL or citation"
    },
    "life_stage_appropriateness": {
      "score": 4.5,
      "framework": "AAHA 2023 Canine Life-Stage Guidelines",
      "evidence_grade": "Tier 4",
      "justification": "All age-appropriate care in place, diet matches life stage",
      "source": "URL or citation"
    }
  },
  "overall_score": {
    "weighted_mean": 4.38,
    "grade": "Very Good",
    "interpretation": "High-quality care with minor improvement areas"
  }
}
```

This structured output is passed to the improvement roadmap stage for prioritization.
