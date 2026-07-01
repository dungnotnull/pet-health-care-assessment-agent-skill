---
name: sub-profile-intake
description: (pet-health-care-assessment) Capture species, breed, age, weight and history with an educational/non-diagnostic disclaimer.
---

# Sub-skill: Profile Intake

## Purpose
Capture comprehensive pet profile data including species, breed, age, weight, medical history, and current care practices. Establish an educational/non-diagnostic boundary while gathering sufficient context for framework-based evaluation.

## When the Harness Calls This
Stage matching `sub-profile-intake` in the `pet-health-care-assessment` main workflow. This is the FIRST stage that runs after initial user request parsing.

## Disclaimer Statement (Mandatory)
```
IMPORTANT: This skill provides educational guidance only and is NOT a substitute for
professional veterinary care. If you suspect your pet is experiencing a medical emergency,
contact your veterinarian or an emergency veterinary hospital immediately. This assessment
cannot diagnose, treat, or prescribe for any medical condition.
```

## Required Information Fields

### Core Demographics
1. **Species** - Dog, cat, rabbit, bird, reptile, exotic, other
2. **Breed** - Purebred, mixed breed, specific breed name, or unknown
3. **Age** - In years and months (or life stage: puppy/kitten, adult, senior)
4. **Weight** - Current weight in kg/lbs with body condition context
5. **Sex** - Male, female, neutered/spayed status

### Health History
6. **Current medical conditions** - Diagnosed conditions, chronic diseases, disabilities
7. **Current medications** - Prescription medications, supplements, preventive treatments
8. **Surgical history** - Past surgeries, procedures, hospitalizations
9. **Vaccination status** - Last vaccines received, due dates
10. **Parasite prevention** - Current flea/tick/heartworm prevention regimen

### Current Care Practices
11. **Diet** - Primary food type, brand, feeding schedule, treats/supplements
12. **Exercise** - Type, frequency, duration of physical activity
13. **Living environment** - Indoor/outdoor, housing type, other pets
14. **Behavioral notes** - Any concerns, training history, socialization status
15. **Veterinary care** - Frequency of vet visits, last wellness exam date

### Owner Concerns
16. **Primary concern** - What prompted this assessment
17. **Specific symptoms** - Any current symptoms or changes (if applicable)
18. **Improvement goals** - What the owner hopes to achieve

## Intake Procedure

### Step 1: Present Disclaimer
ALWAYS begin with the mandatory disclaimer statement above. Wait for acknowledgment before proceeding.

### Step 2: Request Core Demographics
```
Please provide the following information about your pet:

1. Species (dog, cat, rabbit, bird, reptile, exotic, other):
2. Breed (if known):
3. Age (years/months or life stage):
4. Current weight:
5. Sex and neuter/spay status:
```

### Step 3: Health History Collection
```
Health History:
6. Any current or past medical conditions?
7. Current medications or supplements?
8. Any past surgeries or procedures?
9. Last vaccination date(s):
10. Current parasite prevention (flea/tick/heartworm):
```

### Step 4: Current Care Practices
```
Current Care:
11. Primary diet (brand, type, feeding schedule):
12. Exercise routine (type, frequency, duration):
13. Living environment (indoor/outdoor, other pets):
14. Behavioral concerns or notes:
15. Last veterinary wellness visit:
```

### Step 5: Owner Concerns
```
Your Goals:
16. What prompted this assessment?
17. Any current symptoms or changes noticed?
18. What would you most like to improve?
```

### Step 6: Validate Completeness
For each field, apply validation rules:
- **Species**: Must be provided. If unknown, ask for clarification on animal type.
- **Age**: Required. If unknown, provide age estimation guidance based on species.
- **Weight**: Required for nutritional assessment. If unknown, flag for priority data collection.
- **Medical conditions**: If owner reports any conditions, request clarification on diagnosis source (vet vs. owner assumption).

### Step 7: Detect Species-Specific Requirements
Based on species identified, trigger additional species-specific intake:

**For Dogs:**
- Activity level (sedentary, moderate, active, working)
- Coat type and grooming needs
- Breed-specific health risks (if purebred)

**For Cats:**
- Indoor/outdoor status
- Litter box habits
- Interaction with other animals

**For Exotics/Reptiles/Birds:**
- Enclosure specifications
- Temperature/humidity requirements
- Specialized dietary needs

## Outputs

### Structured Profile Object (JSON-style structure for harness):
```json
{
  "meta": {
    "disclaimer_acknowledged": true,
    "intake_timestamp": "ISO-8601",
    "species_category": "mammal|bird|reptile|exotic"
  },
  "demographics": {
    "species": "string",
    "breed": "string",
    "age_years": number,
    "age_months": number,
    "life_stage": "pediatric|adult|senior|geriatric",
    "weight_kg": number,
    "weight_lbs": number,
    "body_condition": "underweight|ideal|overweight|obese|unknown",
    "sex": "male|female",
    "reproductive_status": "intact|neutered|spayed|unknown"
  },
  "health_history": {
    "conditions": ["list of diagnosed conditions"],
    "medications": ["list with doses if provided"],
    "surgeries": ["list with dates if known"],
    "last_vaccination": "date or approximate",
    "parasite_prevention": "type and frequency",
    "allergies": ["known allergies if any"]
  },
  "current_care": {
    "diet": {
      "primary_food": "brand/type",
      "feeding_schedule": "description",
      "supplements": ["list"],
      "treats": "frequency/type"
    },
    "exercise": {
      "type": "description",
      "frequency": "description",
      "duration": "description"
    },
    "environment": {
      "housing": "indoor|outdoor|both",
      "companions": ["other pets"],
      "enrichment": "toys/activities"
    },
    "behavior": {
      "concerns": ["list"],
      "training": "description",
      "socialization": "description"
    },
    "veterinary_care": {
      "last_visit": "date",
      "frequency": "description",
      "clinic": "name if provided"
    }
  },
  "concerns": {
    "primary_reason": "user's main concern",
    "current_symptoms": ["list"],
    "improvement_goals": ["list"]
  },
  "data_quality": {
    "completeness_score": 0.0-1.0,
    "missing_critical_fields": ["list"],
    "uncertain_fields": ["list requiring verification"],
    "flags": ["any data quality concerns"]
  }
}
```

### Species Framework Mapping
Return the appropriate frameworks for the detected species:

| Species | Primary Frameworks | Life Stage Guide |
|---------|-------------------|------------------|
| Dog | AAHA canine life-stage, WSAVA nutrition, Five Domains | Puppy/Adult/Senior/Geriatric |
| Cat | AAHA feline life-stage, AAFP/AAHA nutrition, Five Domains | Kitten/Adult/Senior/Geriatric |
| Rabbit | RCVS/BSAVA rabbit welfare, House Rabbit Society guidelines | Junior/Adult/Senior |
| Bird | AAAV (avian), Five Domains adaptation | Hatchling/Juvenile/Adult/Senior |
| Reptile | ARV reptile welfare, Five Domains adaptation | Hatchling/Juvenile/Adult/Senior |
| Exotic | Species-specific guidelines, Five Domains | Varies by species |

## Evidence Grading During Intake
For any factual claims made during intake (e.g., "grain-free diets cause heart disease"), apply evidence hierarchy:
- **Systematic Review/Meta-Analysis** (Tier 1)
- **Randomized Controlled Trial** (Tier 2)
- **Cohort Study** (Tier 3)
- **Expert Consensus/Guidelines** (Tier 4)
- **Case Reports/Opinion** (Tier 5)
- **Unverified Claims** (Tier 6)

If user makes a claim requiring verification, note it for research phase: `[RESEARCH-NEED: verify claim X]`

## Quality Gate Checklist
Before passing to next stage, verify:
- [ ] Disclaimer presented and acknowledged
- [ ] Species identified with confidence
- [ ] Age and weight obtained (or flagged as critical missing)
- [ ] At minimum: diet, exercise, and basic health history collected
- [ ] Species-appropriate frameworks mapped
- [ ] Data quality score calculated
- [ ] Any critical missing information flagged for follow-up

## Edge Cases and Handling

### If User Refuses to Provide Information
- Acknowledge the limitation
- Proceed with available information
- Flag in data_quality: "user declined to provide [field]"
- Adjust confidence levels in subsequent analysis

### If Information Appears Inaccurate
- Note the concern in data_quality flags
- Request clarification politely
- If unresolved, note uncertainty in relevant sections

### If Multiple Pets Present
- Request clarification on which pet is being assessed
- If simultaneous assessment needed, run separate intake for each
- Do not mix data from multiple animals

### If Species Is Unusual/Exotic
- Still apply Five Domains framework
- Note any framework limitations for species
- Search for species-specific guidance in research phase
