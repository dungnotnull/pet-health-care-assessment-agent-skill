---
name: sub-safety-screener
description: (pet-health-care-assessment) Screen for veterinary emergency red flags FIRST and route urgent cases to a vet/ER.
---

# Sub-skill: Safety Screener

## Purpose
Screen ALL inputs for veterinary emergency red flags BEFORE any guidance is provided. Route urgent cases to immediate professional care. This is the MANDATORY FIRST gate in the harness.

## When the Harness Calls This
Stage matching `sub-safety-screener` in the `pet-health-care-assessment` main workflow. This runs TWICE:
1. **Pre-assessment** - Immediately after intake, before any scoring or guidance
2. **Pre-output** - Final verification before delivering recommendations

## Emergency Triage Protocol

### Immediate Emergency Red Flags (ESCALATE NOW)
If ANY of these are present, STOP the entire assessment and provide emergency resources only:

#### Life-Threatening Indicators
| Category | Red Flag Symptoms | Action |
|----------|-------------------|--------|
| Respiratory | - Labored breathing, gasping, open-mouth breathing (cats)<br>- Blue/gray gums or tongue<br>- Choking or gagging<br>- Respiratory rate >60 breaths/min (dogs) or >40 (cats) | **IMMEDIATE VET ER** |
| Cardiovascular | - Pale or white gums<br>- Weak/absent pulse<br>- Collapse or fainting<br>- Rapid heart rate >180 (dogs) or >220 (cats) at rest | **IMMEDIATE VET ER** |
| Neurological | - Seizures lasting >5 minutes or multiple seizures<br>- Loss of consciousness/coma<br>- Inability to stand or walk<br>- Head tilt, circling, abnormal eye movements | **IMMEDIATE VET ER** |
| Gastrointestinal | - Abdominal distension with dry-heaving (GDV sign)<br>- Vomiting blood or dark coffee-ground material<br>- Bloody diarrhea with collapse<br>- Known or suspected toxin ingestion (within 2 hrs) | **IMMEDIATE VET ER** |
| Trauma | - Hit by car, fall from height<br>- Deep wounds or bleeding that won't stop<br>- Bone protruding from skin<br>- Uncontrolled bleeding | **IMMEDIATE VET ER** |
| Urinary | - Straining to urinate with no output (especially male cats)<br>- Blood in urine with distress | **IMMEDIATE VET ER** |
| Temperature | - Body temperature <96°F or >106°F<br>- Heat stroke signs (panting, collapse after heat exposure) | **IMMEDIATE VET ER** |
| Reproductive | - Female in labor with >3 hrs between puppies/kittens<br>- Straining >2 hrs with no delivery<br>- Fetal membrane protruding >30 mins with no delivery | **IMMEDIATE VET ER** |

### Urgent (Same-Day) Red Flags
These require veterinary care TODAY but are not immediately life-threatening:

| System | Red Flag Signs |
|--------|----------------|
| Eyes | - Squinting, redness, discharge, cloudiness<br>- Eye bulging from socket<br>- Sudden blindness or bumping into things |
| Musculoskeletal | - Non-weight bearing lameness<br>- Sudden inability to rise<br>- Extreme pain response (yelping, avoidance) |
| Skin/Ears | - Severe allergic reaction (face swelling, hives)<br>- Hot, inflamed ear with head tilt<br>- Large rapidly expanding swelling |
| Appetite/Intake | - Complete anorexia >24 hours<br>- Inability to drink water<br>- Vomiting >3 times in 24 hours (without emergency signs) |
| Behavior | - Sudden aggressive behavior change<br>- Extreme lethargy, unresponsive to stimulation<br>- Hiding, refusing to move for >24 hours |

## Screening Procedure

### Step 1: Parse Input for Red Flag Keywords
Scan the intake and user input for emergency indicators. Check for:

**Direct symptom mentions**:
- Breathing difficulties, trouble breathing
- Seizures, convulsions, fitting
- Collapse, fainting, passed out
- Not urinating, straining to pee (especially male cats)
- Vomiting blood, bloody stool
- Choking, gagging, something stuck
- Bleeding that won't stop
- Known toxin ingestion (chocolate, rat poison, medications, plants, etc.)
- Trauma (hit by car, fall, attack)
- Distended abdomen + dry heaving (bloat/gdv)

**Contextual urgency indicators**:
- "emergency", "urgent", "need help now"
- "not acting normal", "really sick"
- "scared", "worried", "something is wrong"
- Time-specific: "started suddenly", "happened just now", "getting worse"

### Step 2: Apply Red Flag Decision Tree
```
IF (any IMMEDIATE EMERGENCY flag present):
    RETURN [EMERGENCY_ESCALATION]
    STOP ALL ASSESSMENT

ELSE IF (any URGENT flag present):
    RETURN [URGENT_RECOMMENDATION + SAME-DAY_VET_ADVICE]
    MAY CONTINUE with caution and repeated disclaimer

ELSE:
    RETURN [CLEAR]
    PROCEED to assessment stages
```

### Step 3: Verify Against Species-Specific Risks
Some red flags vary by species:

**Dogs - Additional Red Flags**:
- Bloat (GDV): distended abdomen + retching/dry heaving (deep-chested breeds)
- Heat stroke: heavy panting, collapse after exercise/heat
- Chocolate/toxin ingestion

**Cats - Additional Red Flags**:
- Urinary blockage: straining in litter box with no output (male cats especially)
- Aortic thromboembolism: sudden paralysis/pain in rear legs
- Respiratory distress: open-mouth breathing (cats don't normally pant)

**Rabbits - Additional Red Flags**:
- GI stasis: not eating or pooping >12 hours
- Head tilt: inner ear infection or parasite
- Flystrike: maggots in fur (especially around rear)

**Birds - Additional Red Flags**:
- Sitting at bottom of cage, fluffed
- Tail bobbing with each breath
- Blood in feathers or droppings

**Reptiles - Additional Red Flags**:
- Dysecdysis (abnormal shed): retained shed on eyes/toes
- Mouth rot: swelling, pus in mouth
- Shell rot (turtles): soft/mushy shell areas

## Emergency Escalation Output Format

### When EMERGENCY is Triggered
```
⚠️ EMERGENCY VETERINARY CARE REQUIRED ⚠️

Based on the information provided, your pet may be experiencing a
MEDICAL EMERGENCY that requires IMMEDIATE veterinary attention.

DO NOT WAIT. Contact one of these resources NOW:

📞 Emergency Veterinary Hospitals:
- [If location known, search local emergency vets]
- "Emergency vet near me" - Google Maps
- "Emergency animal hospital [your city]"
- Animal Poison Control: (888) 426-4435 (US/Canada) - fee applies

🚪 If you cannot reach a veterinarian:
- Transport to the nearest emergency veterinary hospital
- Do NOT give human medications unless directed by a vet
- Do NOT offer food if vomiting, bloat, or anesthesia might be needed

⏱️ TIME IS CRITICAL in emergencies. Delaying care can be fatal.

[Specific red flag detected]: [brief description]
[Why this is urgent]: [medical explanation]

This assessment cannot provide emergency guidance. Please seek
immediate professional veterinary care.
```

### When URGENT is Triggered
```
⚠️ URGENT VETERINARY CARE RECOMMENDED TODAY ⚠️

Based on the information provided, your pet should be examined by
a veterinarian TODAY (within 12-24 hours).

Please schedule a SAME-DAY appointment with your veterinarian or
visit an urgent care veterinary facility.

[Specific concerns detected]: [list]

While you arrange veterinary care:
[Species-appropriate home precautions, if any]

This assessment provides educational information only and does not
replace professional veterinary examination and treatment.
```

## Framework-Specific Safety Thresholds

### AAHA Life-Stage Care Guidelines - Emergency Signs
Per AAHA, these warrant immediate evaluation regardless of life stage:
- Acute collapse or loss of consciousness
- Severe respiratory distress
- Uncontrolled bleeding or trauma
- Suspected poisoning/toxin exposure
- Obstetric emergencies

### WSAVA Nutrition - Red Flags
Nutritional emergencies requiring immediate vet care:
- GDV/bloat (gastric dilatation-volvulus)
- Foreign body obstruction (ingestion of objects)
- Acute pancreatitis signs
- Severe electrolyte abnormalities

### Five Domains Model - Critical Welfare Failures
Domain 1 (Nutrition): Complete anorexia >24-48 hours
Domain 2 (Environment): Temperature extremes, lack of water access
Domain 3 (Health): Any of the emergency indicators above
Domain 4 (Behavior): Extreme fear/panic indicating pain/distress
Domain 5 (Mental State): Depression, complete inactivity

## Quality Gates

### Pre-Assessment Gate
Before ANY scoring or guidance begins:
- [ ] Red flag screening completed
- [ ] Emergency escalation issued if needed
- [ ] Only continue if status is CLEAR or URGENT with explicit owner acknowledgment
- [ ] If emergency, assessment HALTED completely

### Pre-Output Gate
Before delivering ANY recommendations:
- [ ] Re-verify no emergency conditions were described
- [ ] Include disclaimer prominently
- [ ] If ANY uncertainty exists, re-state veterinary referral

## Output Status Codes

| Status | Meaning | Action |
|--------|---------|--------|
| EMERGENCY | Life-threatening condition detected | STOP; provide emergency resources only |
| URGENT | Serious condition requiring same-day care | Continue with caution; prominent vet referral |
| CLEAR | No emergency indicators detected | Proceed with full assessment |
| UNCLEAR | Insufficient information to rule out emergency | Ask clarifying questions before proceeding |

## Research-First Verification
For borderline cases, use WebSearch to verify:
- "[species] [symptom] when to see vet emergency"
- "[species] [symptom] urgent care criteria"
- "[species] toxic substance ingestion timeline"

Apply evidence hierarchy to determine if escalation is warranted based on best-practice guidelines.

## Edge Cases

### User Downplays Severity
If user says "not that bad" but describes red flags:
- Acknowledge their assessment
- Present objective criteria
- Strongly recommend veterinary evaluation
- Document the discrepancy

### User Asks for Home Remedies for Emergency
- Decline to provide home remedies
- Explain why veterinary care is essential
- Offer to help locate veterinary resources
- Cite objective reasons for escalation

### User Cannot Afford Emergency Care
- Acknowledge the financial difficulty
- Provide resources for financial assistance:
  - CareCredit veterinary financing
  - Local veterinary schools (often lower cost)
  - Animal welfare organizations
  - Payment plan options with clinics
- Still recommend emergency care if life-threatening

### Geographic Constraints (Remote Areas)
- Help locate nearest available care
- If truly unavailable, provide FIRST AID ONLY with repeated disclaimer
- Note this is temporary stabilization only, not definitive care
- Repeatedly emphasize need for veterinary follow-up
