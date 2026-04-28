# Code Review Checklist

Standard checklist for council reviews using `@council-orchestrator`.

---

## When to Use This Checklist

- After major feature implementation
- Before merging to main branch
- When refactoring critical code
- After fixing security issues

---

## Review Process

### 1. Invoke Council Orchestrator
```
/task council-orchestrator
Review the code in @04_Active_Work/{task-name} for security, performance, code quality, and documentation.
```

### 2. Orchestrator Delegates to:
- **@council-security** - Security vulnerabilities
- **@council-performance** - Performance bottlenecks
- **@council-quality** - Code quality & best practices
- **@council-docs** - Documentation completeness
- **@council-architect** - Architecture & design (if relevant)

---

## Security Review (@council-security)

### Critical Checks
- [ ] No API keys or secrets in code
- [ ] Input validation on all user inputs
- [ ] Authentication/authorization properly implemented
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] CSRF protection enabled
- [ ] Security headers set (CSP, HSTS, etc.)
- [ ] Sensitive data encrypted at rest and in transit
- [ ] Dependency vulnerabilities checked (`npm audit`)

### Severity Levels
| Level | Action |
|-------|--------|
| Critical | Must fix before merge |
| High | Should fix before merge |
| Medium | Fix in follow-up PR |
| Low | Can defer to future |
| Info | Awareness only |

---

## Performance Review (@council-performance)

### Checks
- [ ] Algorithm complexity acceptable (Big O noted)
- [ ] Database queries optimized (no N+1 problems)
- [ ] Memory usage reasonable (no obvious leaks)
- [ ] Async/await used correctly (no blocking calls)
- [ ] Bundle size impact assessed (if frontend)
- [ ] Caching strategy appropriate
- [ ] Resource cleanup implemented (dispose/cleanup)

### Impact Levels
| Level | Action |
|-------|--------|
| Critical | Causes timeouts/ OOM → Must fix |
| High | Noticeable slowdown → Should fix |
| Medium | Minor inefficiency → Fix when time permits |
| Low | Optimization opportunity → Consider for future |

---

## Code Quality Review (@council-quality)

### Checks
- [ ] Code follows project conventions
- [ ] No code smells (long methods, deep nesting)
- [ ] DRY principle followed (no duplication)
- [ ] Meaningful variable/function names
- [ ] Error handling implemented
- [ ] Edge cases covered
- [ ] Tests provided (unit + integration)
- [ ] Test coverage acceptable (>80% for critical code)
- [ ] Comments where necessary (not obvious code)
- [ ] No commented-out code left in

### Priority Levels
| Level | Action |
|-------|--------|
| Must Fix | Blocks merge |
| Should Fix | Improves maintainability |
| Consider | Nice to have |
| Nice to Have | Optional |

---

## Documentation Review (@council-docs)

### Checks
- [ ] API documentation complete (if applicable)
- [ ] Code comments adequate
- [ ] README updated (if user-facing change)
- [ ] Architecture docs updated (if design changed)
- [ ] JSDoc/docstrings added to functions
- [ ] Examples provided for complex logic
- [ ] CHANGELOG updated (if release-related)

### Priority Levels
| Level | Action |
|-------|--------|
| Critical (blocking) | Docs must be complete before merge |
| Important | Should be added |
| Helpful | Improves usability |
| Optional | Can defer |

---

## Architecture Review (@council-architect)

### Checks (if applicable)
- [ ] Follows established patterns
- [ ] Proper separation of concerns
- [ ] API design appropriate (REST/GraphQL/etc.)
- [ ] Module boundaries respected
- [ ] Dependency direction correct (no circular deps)
- [ ] Scalability considerations addressed
- [ ] Integration points documented

---

## Review Summary Template

Council orchestrator provides unified summary:

```markdown
# Council Review: {Task Name}

**Date**: YYYY-MM-DD  
**Reviewer**: council-orchestrator (with security, performance, quality, docs)

---

## Executive Summary
[1-2 paragraph overview of findings]

---

## Findings by Council Member

### @council-security
| Severity | Finding | Location |
|----------|---------|----------|
| Critical | [Finding] | [File:Line] |
| High | [Finding] | [File:Line] |

### @council-performance
| Impact | Finding | Location |
|--------|---------|----------|
| High | [Finding] | [File:Line] |

### @council-quality
| Priority | Finding | Location |
|----------|---------|----------|
| Must Fix | [Finding] | [File:Line] |

### @council-docs
| Priority | Finding | Location |
|----------|---------|----------|
| Important | [Finding] | [File:Line] |

---

## Unified Recommendation

### Must Fix Before Merge
1. [Issue 1] - [How to fix]
2. [Issue 2] - [How to fix]

### Should Fix (Soon)
1. [Issue 1]
2. [Issue 2]

### Consider for Future
1. [Improvement 1]
2. [Improvement 2]

---

## Verdict
[ ] **APPROVE** - Ready to merge
[ ] **APPROVE WITH MINOR FIXES** - Fix issues, no re-review needed
[ ] **REQUEST CHANGES** - Fix issues and re-review required
```

---

## Quick Commands

| Action | Command |
|--------|----------|
| Full council review | `/task council-orchestrator` then describe review scope |
| Security only | `@council-security Review @path/to/code` |
| Performance only | `@council-performance Analyze @path/to/code` |
| Quality only | `@council-quality Check @path/to/code` |
| Docs only | `@council-docs Review docs in @path` |

---

## After Review

1. **Address feedback** - Fix issues identified
2. **Re-run tests** - Ensure fixes don't break anything
3. **Update session log** - `04_Active_Work/session-YYYY-MM-DD.md`
4. **Update memory** - `MEMORY.md` with lessons learned
5. **Commit fixes** - Clear commit messages referencing review
