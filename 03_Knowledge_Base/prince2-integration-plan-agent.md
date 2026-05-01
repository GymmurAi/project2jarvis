# Research: PRINCE2 Elements for Plan Agent Integration

**Date**: 2026-05-01  
**Researcher**: @researcher  
**Purpose**: Identify relevant PRINCE2 project management elements to integrate into Plan Agent

---

## Executive Summary

PRINCE2 (Projects IN Controlled Environments) is a structured project management methodology with 7 principles, 7 themes, and 7 processes. After analyzing all elements, **5 principles, 4 themes, and 3 processes** are highly relevant to our Plan Agent and should be integrated. The remaining elements are either already covered by our 6-phase process or not applicable to AI agent workflows.

**Key Finding**: PRINCE2's "Manage by Exception" and "Continued Business Justification" principles align perfectly with our Plan Agent's role as gatekeeper preventing system-breaking changes.

---

## PRINCE2 Core Elements

### The 7 Principles (Foundation - Cannot be tailored)

| # | Principle | Definition | Relevance to Plan Agent | Integration Priority |
|---|-----------|-------------|--------------------------|------------------------|
| 1 | **Continued Business Justification** | Project must have valid business case throughout | ✅ **HIGH** - Every plan needs "Why are we doing this?" section | **P0 - Integrate immediately** |
| 2 | **Learn from Experience** | Use lessons from past projects | ✅ **HIGH** - Already partially done (reads postmortem), needs formal "Lessons Log" | **P0 - Enhance existing** |
| 3 | **Defined Roles & Responsibilities** | Clear accountability structure | ✅ **HIGH** - Agent Coordination Map already implements this | **P1 - Formalize** |
| 4 | **Manage by Stages** | Break project into manageable stages | ✅ **HIGH** - Our 6-phase process IS stage management | **Already implemented** |
| 5 | **Manage by Exception** | Only escalate when tolerances exceeded | ✅ **HIGH** - Plan Agent IS the exception management layer | **P0 - Document this** |
| 6 | **Focus on Products** | Deliverables-defined approach | ⚠️ **MEDIUM** - We focus on process, not products | **P2 - Consider adding** |
| 7 | **Tailor to Suit Project** | Adapt methodology to context | ✅ **HIGH** - Two-tier templates (Lite/Full) already implement this | **Already implemented** |

---

### The 7 Themes (Ongoing Project Management Areas)

| # | Theme | Definition | Relevance to Plan Agent | Integration Priority |
|---|------|-------------|--------------------------|------------------------|
| 1 | **Business Case** | Maintain viability justification | ✅ **HIGH** - Aligns with Principle 1 | **P0 - Add to Phase 1** |
| 2 | **Organization** | Project team structure | ✅ **HIGH** - Agent Coordination Map covers this | **P1 - Expand** |
| 3 | **Quality** | Define & achieve quality standards | ⚠️ **MEDIUM** - Council review partially covers | **P2 - Add quality criteria** |
| 4 | **Plans** | How/when objectives achieved | ✅ **HIGH** - Our entire planning process | **Already implemented** |
| 5 | **Risk** | Identify, assess, manage threats | ✅ **HIGH** - Risk Assessment section exists | **P1 - Enhance with frameworks** |
| 6 | **Change** | Handle change requests systematically | ❌ **LOW** - Not applicable to AI agents (no human change requests) | **Skip** |
| 7 | **Progress** | Monitor vs. plans, report status | ✅ **HIGH** - Phase 5 (Monitoring) covers this | **P1 - Add metrics** |

---

### The 7 Processes (Step-by-Step Workflow)

| # | Process | Definition | Relevance to Plan Agent | Integration Priority |
|---|---------|-------------|--------------------------|------------------------|
| 1 | **Starting up a Project (SU)** | Pre-project, check viability | ✅ **HIGH** - Maps to our Phase 1 (Idea Analysis) | **Already implemented** |
| 2 | **Initiating a Project (IP)** | Define project, set tolerances | ✅ **HIGH** - Maps to our Phase 2 (Risk Assessment) + Phase 3 (Plan Creation) | **P1 - Add tolerance definition** |
| 3 | **Directing a Project (DP)** | Project board oversight | ❌ **LOW** - No human board in AI system | **Skip** |
| 4 | **Controlling a Stage (CS)** | Day-to-day management | ✅ **HIGH** - Maps to our Phase 4 (Delegation) + Phase 5 (Monitoring) | **Already implemented** |
| 5 | **Managing Product Delivery (MP)** | Team manager delivers products | ⚠️ **MEDIUM** - Builder agent delivers, but no "product" focus | **P2 - Shift focus slightly** |
| 6 | **Managing Stage Boundaries (SB)** | Review stage, authorize next | ✅ **HIGH** - Our "verify each step before proceeding" rule | **P1 - Formalize checkpoints** |
| 7 | **Closing a Project (CP)** | Confirm handover, lessons learned | ✅ **HIGH** - Our Phase 6 (Verification) + session logs | **P1 - Add lessons capture** |

---

## Elements to Integrate (Priority Breakdown)

### P0 - Integrate Immediately (Before Full Deployment)

#### 1. Principle 1: Continued Business Justification
**What to Add**:
- **Phase 1 (Idea Analysis)**: Add "Business Case" section
  - Why are we doing this? (mandatory)
  - Expected benefits (quantifiable if possible)
  - Viability check: "Does this align with project goals?"
  - Ongoing justification: "When would we stop this project?"

**Implementation**:
```markdown
## 1. Idea Analysis

### Business Case (PRINCE2 Principle 1)
- **Why**: {mandatory - what's the business/user value?}
- **Benefits**: {quantifiable if possible}
- **Viability**: Does this align with Project2Jarvis goals?
- **Stop Conditions**: When would we cancel this project?
```

#### 2. Principle 5: Manage by Exception
**What to Add**:
- Document that Plan Agent IS the "exception management" layer
- Define tolerances for delegated agents:
  - Time tolerance: "If builder takes >2 hours, escalate"
  - Quality tolerance: "If 2+ council issues, escalate"
  - Dependency tolerance: "If npm ls shows conflicts, stop"

**Implementation**:
```markdown
## 5. Monitoring (PRINCE2 Principle 5: Manage by Exception)

### Tolerances (Delegation Limits)
| Agent | Time Tolerance | Quality Tolerance | Dependency Tolerance |
|-------|----------------|-------------------|------------------------|
| researcher | 1 hour | N/A | N/A |
| builder | 2 hours | Max 3 council issues | No conflicts allowed |
| council | 1 hour | N/A | N/A |

### Exception Escalation
If tolerances exceeded → Plan Agent intervenes → User notified
```

#### 3. Principle 2: Learn from Experience (Enhance)
**What to Add**:
- Formal "Lessons Log" section in every plan
- Mandatory: Read `03_Knowledge_Base/lessons-learned.md` at start
- After completion: Log new lessons to same file

**Implementation**:
```markdown
## 2. Risk Assessment

### Lessons Log (PRINCE2 Principle 2)
- **Past Lessons Applied**: {from lessons-learned.md}
- **New Lessons Identified**: {during planning}
- **Post-Completion**: Log to lessons-learned.md
```

#### 4. Theme 1: Business Case (Align with Principle 1)
**What to Add**: Already covered above in Principle 1 integration.

---

### P1 - Should Add (Before Full "MANDATORY" Enforcement)

#### 5. Process 2: Initiating a Project - Tolerance Definition
**What to Add**:
- Define "tolerances" for each agent in the plan
- Time, cost (if applicable), quality, scope tolerances
- If exceeded → exception → Plan Agent intervenes

**Implementation**: Add "Tolerances" table to Phase 3 (Plan Creation).

#### 6. Process 6: Managing Stage Boundaries - Formal Checkpoints
**What to Add**:
- After each phase: "Checkpoint - Proceed to next phase?"
- Formal "Stage Boundary Review" before Phase 4 (Delegation)
- User sign-off required for complex projects

**Implementation**: Add checkpoint prompts between phases in plan-agent.md.

#### 7. Theme 5: Risk (Enhance with Framework)
**What to Add**:
- Use FAIR risk framework (Feasibility, Acceptability, Inherent, Residual)
- Or simple: Probability × Impact matrix with mitigation

**Implementation**: Enhance "Risk Assessment" section with quantitative scoring.

#### 8. Theme 7: Progress (Add Metrics)
**What to Add**:
- Track: Time spent vs. estimate
- Track: Number of exceptions escalated
- Track: Council issues found
- Post-project: Compare plan vs. actual

**Implementation**: Add "Progress Tracking" to Phase 5 (Monitoring).

#### 9. Principle 3: Defined Roles (Formalize)
**What to Add**:
- Already have Agent Coordination Map
- Formalize: "Project Board" = User, "Project Manager" = Plan Agent, "Team Manager" = Builder, etc.
- Add PRINCE2 role mappings to Plan Agent documentation

**Implementation**: Add "PRINCE2 Role Mapping" section to plan-agent.md.

---

### P2 - Nice to Have (Future Iterations)

#### 10. Principle 6: Focus on Products (Shift Emphasis)
**What to Add**:
- Define "Products" (deliverables) more clearly
- Each phase should have clear "Product Description"
- Quality criteria for each product

**Implementation**: Add "Product Descriptions" to each phase in planning template.

#### 11. Theme 3: Quality (Add Quality Criteria)
**What to Add**:
- Define "Quality Expectations" for each agent
- Acceptance criteria beyond "build passes"
- User acceptance testing (UAT) for UI projects

**Implementation**: Expand "Success Criteria" section with quality dimensions.

#### 12. Process 7: Closing a Project (Add Lessons Capture)
**What to Add**:
- Mandatory: Log lessons to `lessons-learned.md` at end
- Update `decisions-log.md` with ADR
- Session log creation (already done)

**Implementation**: Enhance Phase 6 (Verification) to include formal lessons capture.

---

## Elements to SKIP (Not Applicable)

| Element | Reason for Skipping |
|---------|----------------------|
| **Process 3: Directing a Project** | No human "Project Board" in AI system |
| **Theme 6: Change** | AI agents don't receive human change requests |
| **Principle 3 (Roles)** - partial | Already covered by Agent Coordination Map |
| **Process 5: Managing Product Delivery** | Too focused on "products" vs. our "process" approach |

---

## Integration Plan for Plan Agent

### Step 1: Update `plan-agent.md` (P0 Changes)

Add to **Phase 1 (Idea Analysis)**:
```markdown
### Business Case (PRINCE2 Principle 1)
- **Why**: {mandatory}
- **Benefits**: {quantifiable}
- **Viability**: Aligns with Project2Jarvis goals?
- **Stop Conditions**: When would we cancel?
```

Add to **Phase 5 (Monitoring)**:
```markdown
### Exception Management (PRINCE2 Principle 5)
| Agent | Time Tolerance | Quality Tolerance | Dependency Tolerance |
|-------|----------------|-------------------|------------------------|
| researcher | 1 hour | N/A | N/A |
| builder | 2 hours | Max 3 council issues | No conflicts allowed |

If tolerances exceeded → Exception escalated to Plan Agent
```

Add to **Memory Protocol (Session Start)**:
```markdown
2. Read `03_Knowledge_Base/lessons-learned.md` - past lessons (PRINCE2 Principle 2)
```

### Step 2: Update `planning-template.md` (P0 Changes)

Add to **Section 1 (Idea Analysis)**:
```markdown
### Business Case (PRINCE2 Principle 1)
- **Why**: {mandatory - what's the business/user value?}
- **Benefits**: {quantifiable if possible}
- **Viability**: Does this align with Project2Jarvis goals?
- **Stop Conditions**: When would we cancel this project?
```

Add to **Section 2 (Risk Assessment)**:
```markdown
### Lessons Log (PRINCE2 Principle 2)
- **Past Lessons Applied**: {from lessons-learned.md}
- **New Lessons Identified**: {during planning}
```

### Step 3: Document PRINCE2 Integration (New File)

Create `03_Knowledge_Base/prince2-integration-plan-agent.md` with:
- This research summary
- Mapping of PRINCE2 elements to our 6-phase process
- Implementation checklist

---

## PRINCE2 ↔ Plan Agent Mapping

| PRINCE2 Element | Plan Agent Equivalent |
|----------------|------------------------|
| **Principle 1: Business Justification** | Phase 1 - Business Case section |
| **Principle 2: Learn from Experience** | Read lessons-learned.md, postmortem |
| **Principle 4: Manage by Stages** | 6-Phase Process (Analyze → Assess → Plan → Delegate → Monitor → Verify) |
| **Principle 5: Manage by Exception** | Plan Agent IS the exception layer, tolerances defined |
| **Principle 7: Tailor to Suit** | Two-tier templates (Lite/Full) |
| **Theme 1: Business Case** | Phase 1 - Business Case section |
| **Theme 5: Risk** | Phase 2 - Risk Assessment section |
| **Theme 7: Progress** | Phase 5 - Monitoring section |
| **Process 1: Starting up (SU)** | Phase 1 - Idea Analysis |
| **Process 2: Initiating (IP)** | Phase 2 + Phase 3 - Risk + Plan |
| **Process 4: Controlling a Stage (CS)** | Phase 4 + 5 - Delegation + Monitoring |
| **Process 6: Managing Stage Boundaries (SB)** | Checkpoints between phases |

---

## Sources

1. [Understanding the seven principles in PRINCE2](https://www.prince2.com/uk/blog/understanding-the-seven-principles-in-prince2) - PRINCE2 UK, 2023-06-15
2. [What is PRINCE2: Core Elements](https://taskford.com/en/blog/prince2-methodology) - TaskFord
3. [PRINCE2 Methodology Explained](https://www.prince2.com/eur/prince2-methodology) - PRINCE2 Official
4. [PRINCE2 Wikipedia](https://en.wikipedia.org/wiki/PRINCE2) - Wikipedia
5. [How Does PRINCE2 Work?](https://www.professionaldevelopment.ie/how-does-prince2-work) - Professional Development
6. [Core principles - PRINCE2 Wiki](https://prince2.wiki/principles/) - Frank Turley
7. [PRINCE2 Seven Principles Explained](https://www.knowledgehut.com/blog/project-management/the-principles-of-prince2) - KnowledgeHut, 2024-02-18
8. [The 7 principles, practices and processes of PRINCE2](https://www.prince2.com/usa/blog/the-7-principles-themes-and-processes-of-prince2) - PRINCE2 USA, 2016-09-19

---

## Metadata

- **Date**: 2026-05-01
- **Researcher**: @researcher (Plan Agent PRINCE2 Integration)
- **Confidence**: High
- **Tags**: `#prince2` `#plan-agent` `#project-management` `#business-justification` `#exception-management`
- **Related Research**: 
  - `03_Knowledge_Base/plan-agent-research.md`
  - `03_Knowledge_Base/council-review-plan-agent.md`
  - `04_Active_Work/planning-template.md`

---

## Change Log

| Date | Change |
|------|--------|
| 2026-05-01 | Initial research on PRINCE2 elements |
| 2026-05-01 | Identified 5 principles, 4 themes, 3 processes to integrate |
| 2026-05-01 | Created P0/P1/P2 integration plan |
| 2026-05-01 | Mapped PRINCE2 elements to 6-phase process |
