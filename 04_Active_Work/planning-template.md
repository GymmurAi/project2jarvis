# Planning Template: {Idea Name}

**Date**: YYYY-MM-DD  
**Plan Agent**: @plan-agent  
**Status**: DRAFT | READY | IN_PROGRESS | COMPLETED  

---

## Executive Summary

{Brief 1-2 sentence description of the idea and planned approach}

---

## 1. Idea Analysis

### Business Case (PRINCE2 Principle 1)
- **Why**: {mandatory - what's the business/user value?}
- **Benefits**: {quantifiable if possible}
- **Viability**: Does this align with Project2Jarvis goals?
- **Stop Conditions**: When would we cancel this project?

### Request Source
- **From**: {user/agent}
- **Date**: YYYY-MM-DD
- **Original Request**: "{quote the user's exact request}"

### Understanding
{Break down what they're asking for - be specific about scope}

### Project Context
- **Relevant Files**: 
  - {list files that might be affected}
- **Current Dependencies**: 
  - {list relevant packages/versions}
- **Architecture Impact**: 
  - {how does this fit into overall system?}

---

## 2. Risk Assessment

### Lessons Log (PRINCE2 Principle 2)
- **Past Lessons Applied**: {from lessons-learned.md}
- **New Lessons Identified**: {during planning}
- **Post-Completion**: Log to lessons-learned.md

### Dependency Risks 📦
| Risk | Impact | Mitigation |
|------|--------|------------|
| {e.g., Three.js version conflict} | {high/medium/low} | {e.g., Use verified matrix from postmortem} |
| {e.g., New package breaks existing} | {impact} | {mitigation} |

**Check Command**: `npm ls {relevant-packages}`

### Architecture Risks 🏗️
| Risk | Impact | Mitigation |
|------|--------|------------|
| {e.g., Conflicts with existing agent} | {impact} | {mitigation} |
| {e.g., Changes to core system} | {impact} | {mitigation} |

### Design Risks 🎨
| Risk | Impact | Mitigation |
|------|--------|------------|
| {e.g., User rejects design like Exec Command Center} | {high} | {create mockup first, get approval} |

**Reference**: `03_Knowledge_Base/ai-saas-landing-postmortem.md` (design rejection lesson)

### Agent Conflicts ⚠️
| Risk | Impact | Mitigation |
|------|--------|------------|
| {e.g., Multiple agents editing same file} | {high} | {coordinate via plan, one agent at a time} |

### Quantitative Risk Assessment (FAIR/OCTAVE - P2)
| Risk | Probability (1-5) | Impact (1-5) | Score (P×I) | Risk Level | Mitigation |
|------|-------------------|----------------|---------------|------------|------------|
| {risk 1} | 3 | 4 | 12 | Medium | {mitigation} |
| {risk 2} | 5 | 5 | 25 | High | {mitigation} |

**Scoring**: 1-5 scale (1=Very Low, 5=Very High)
**Risk Level**: Low (1-5), Medium (6-15), High (16-25)
**Frameworks**: FAIR (Factor Analysis of Information Risk), OCTAVE (Operationally Critical Threat, Asset, Vulnerability Evaluation)

---

## 3. Dependency Checklist

**MANDATORY - Check before proceeding:**

- [ ] Read `03_Knowledge_Base/ai-saas-landing-postmortem.md` (if 3D project)
- [ ] Run `npm ls {relevant-packages}` to check current state
- [ ] Verify version compatibility matrix (see `03_Knowledge_Base/active-registry.md` Verified Dependency Stacks - ADR-013)
- [ ] Check for peer dependency warnings
- [ ] Document planned versions in this plan

### For 3D Projects ONLY:
```
Stack A (Recommended - Stable):
- three: ^0.170.0
- @react-three/fiber: ^8.17.0
- @react-three/drei: ^9.117.0
- framer-motion: ^11.15.0
- react: ^18.3.1
```

**Reference**: See `[[03_Knowledge_Base/active-registry.md#Verified-Dependency-Stacks]]` for full matrices.

---

## 4. Execution Plan

### Phase 1: Research 🔬
**Agent**: `researcher`  
**Depends On**: -  
**Status**: PENDING | IN_PROGRESS | COMPLETED  

**Tasks**:
1. {task description}
2. {task description}

**Verification**: 
- [ ] Research documented in `03_Knowledge_Base/{topic}.md`
- [ ] Dependency matrix verified
- [ ] Compatibility confirmed

---

### Phase 2: Design 🎨
**Agent**: `{ui-ux-pro-max | 3d-website-architect}`  
**Depends On**: Phase 1  
**Status**: PENDING  

**Tasks**:
1. Create design mockup/prototype
2. Document design decisions
3. Get user approval (MANDATORY)

**Verification**:
- [ ] Design mockup created
- [ ] User approved design
- [ ] Design documented in plan

**⚠️ CRITICAL**: Do NOT proceed to Phase 3 without user design approval!

---

### Phase 3: Implementation 🔨
**Agent**: `builder`  
**Depends On**: Phase 2 (design approved)  
**Status**: PENDING  

**Tasks**:
1. {atomic task 1} → Verify: `npm run build`
2. {atomic task 2} → Verify: `npm run build`
3. {atomic task 3} → Verify: `npm run build`

**Verification**:
- [ ] Each step built successfully
- [ ] `npm ls` shows no conflicts
- [ ] No "ReactCurrentOwner" errors (3D projects)

**Rule**: One change at a time, build after each!

---

### Phase 4: Review 🔍
**Agent**: `council-orchestrator`  
**Depends On**: Phase 3  
**Status**: PENDING  

**Tasks**:
1. Security review
2. Performance review
3. Code quality review

**Verification**:
- [ ] Council review passed
- [ ] No critical issues found

---

### Phase 5: Testing ✅
**Agent**: `agency-evidence-collector`  
**Depends On**: Phase 4  
**Status**: PENDING  

**Tasks**:
1. Write Playwright tests
2. Run test suite
3. Capture evidence (screenshots/videos)

**Verification**:
- [ ] All tests passing
- [ ] No runtime errors
- [ ] Evidence collected

---

### Phase 6: Documentation 📝
**Agent**: `researcher` or `council-docs`  
**Depends On**: Phase 5  
**Status**: PENDING  

**Tasks**:
1. Update relevant docs
2. Update `active-registry.md`
3. Log decision in `decisions-log.md`

**Verification**:
- [ ] Documentation updated
- [ ] Decision logged
- [ ] Session log created

---

## 5. Agent Coordination Matrix

| Step | Agent | Task | Status | Verification |
|------|-------|------|--------|-------------|
| 1 | researcher | Dependency research | PENDING | Research doc created |
| 2 | ui-ux-pro-max | Design mockup | PENDING | User approval |
| 3 | builder | Implement feature | PENDING | Build passes |
| 4 | council-orchestrator | Review code | PENDING | Review passed |
| 5 | agency-evidence-collector | Test functionality | PENDING | Tests pass |
| 6 | researcher | Document changes | PENDING | Docs updated |

---

## 6. Success Criteria

- [ ] **Build**: `npm run build` passes with no errors
- [ ] **Tests**: `npx playwright test` all passing
- [ ] **Design**: User approved (if UI project)
- [ ] **Dependencies**: `npm ls` shows no conflicts
- [ ] **Review**: Council review passed
- [ ] **Documentation**: All docs updated
- [ ] **No Regressions**: Existing features still work

---

## 7. Rollback Plan

If any step fails:

1. **Dependency Conflict**: 
   - Revert to versions in postmortem compatibility matrix
   - Run `npm ls` to verify

2. **Build Failure**:
   - Check git status
   - Revert last change: `git revert HEAD`
   - Re-plan with different approach

3. **Design Rejected**:
   - Like Executive Command Center failure
   - Do NOT proceed to implementation without approval
   - Create new mockup based on feedback

4. **Test Failures**:
   - Fix one test at a time
   - Re-run tests after each fix
   - Document issues in `06_Audit_Logs/`

---

## 8. Timeline Estimate

| Phase | Estimated Time | Actual Time |
|-------|----------------|-------------|
| Research | {X hours} | {fill later} |
| Design | {X hours} | {fill later} |
| Implementation | {X hours} | {fill later} |
| Review | {X hours} | {fill later} |
| Testing | {X hours} | {fill later} |
| Documentation | {X hours} | {fill later} |
| **Total** | **{X hours}** | **{fill later}** |

---

## 9. Notes & Decisions

### Decision 1: {Decision Title}
**Date**: YYYY-MM-DD  
**Decision**: {what was decided}  
**Rationale**: {why}  
**ADR Reference**: ADR-XXX (if applicable)

---

## 10. Sign-off

- [ ] **Plan Agent**: Plan created and verified
- [ ] **User**: Idea approved
- [ ] **Design**: Mockup approved (if applicable)
- [ ] **Council**: Review passed
- [ ] **Builder**: Implementation complete
- [ ] **Tests**: All passing

---

**Plan Status**: {DRAFT | READY | IN_PROGRESS | COMPLETED}  
**Next Step**: {what happens next}

---

**Quick Links**:
- Postmortem: `03_Knowledge_Base/ai-saas-landing-postmortem.md`
- Active Registry: `03_Knowledge_Base/active-registry.md`
- Architecture: `00_Meta/ARCHITECTURE.md`
- Agent Definitions: `.opencode/agents/`
