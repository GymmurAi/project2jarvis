---
name: council
description: Port of Anthropic's Claude Code council concept - a multi-agent system where specialized council members review code and provide comprehensive feedback
license: MIT
compatibility: opencode
metadata:
  version: 1.0.0
  author: Ported from Anthropic Claude Code
  use-case: code-review
---

# Council - Multi-Agent Code Review System

This skill implements a council of specialized AI agents that collaborate to review, analyze, and improve code. Originally designed for Anthropic's Claude Code, this is a port for OpenCode.

## What is the Council?

The Council is a multi-agent system where specialized agents (the "council members") each review code from their area of expertise:

- **council-orchestrator** - Coordinates the council and synthesizes results (primary agent)
- **council-architect** - Reviews system design, architecture, and code organization
- **council-security** - Identifies security vulnerabilities and risks
- **council-performance** - Analyzes performance bottlenecks and optimization opportunities
- **council-quality** - Assesses code quality, best practices, and maintainability
- **council-docs** - Reviews documentation completeness and clarity

## When to Use This Skill

Use the council system when you need:

1. **Comprehensive code reviews** - Before merging critical PRs
2. **Architecture decisions** - When designing new features or refactoring
3. **Security audits** - Before deploying to production
4. **Performance optimization** - When diagnosing slow code
5. **Code quality improvement** - When establishing or enforcing standards

## How to Use

### Switching to the Council Orchestrator

```
/task council-orchestrator
```

Or use the **Tab** key to cycle through primary agents until you reach "council-orchestrator".

### Invoking Specific Council Members

You can @ mention specific council members:

```
@council-security Review this authentication code for vulnerabilities: @src/auth/login.ts
@council-performance Analyze the performance of this function: @src/utils/heavy-computation.ts
```

### Running a Full Council Review

As the orchestrator, simply describe what you want reviewed:

```
Review the new user registration feature in @src/features/registration for architecture, security, performance, code quality, and documentation.
```

The orchestrator will:
1. Analyze your request
2. Delegate to relevant council members using the Task tool
3. Synthesize all feedback
4. Present a unified recommendation

## Council Members

### @council-orchestrator
**Role**: Primary coordinator
**Mode**: Primary agent (switch with Tab)
**When to use**: For coordinating full council reviews

### @council-architect
**Role**: System design and architecture
**Expertise**: Design patterns, SOLID principles, modularity, API design
**When to use**: Reviewing new features, refactoring, or architectural decisions

### @council-security
**Role**: Security review
**Expertise**: OWASP Top 10, CWE, injection attacks, auth flaws, data exposure
**When to use**: Before deploying auth changes, handling sensitive data, or security audits

### @council-performance
**Role**: Performance optimization
**Expertise**: Algorithm complexity, database queries, memory leaks, caching
**When to use**: Diagnosing slow code, optimizing hot paths, or reviewing resource usage

### @council-quality
**Role**: Code quality and best practices
**Expertise**: Code smells, DRY principle, naming conventions, error handling, tests
**When to use**: Establishing coding standards, reviewing PRs, or improving maintainability

### @council-docs
**Role**: Documentation review
**Expertise**: API docs, README, comments, docstrings, technical writing
**When to use**: Reviewing documentation, improving code comments, or writing guides

## Example Workflows

### Full Code Review
```
/council-orchestrator
Review the implementation in @src/payment-processor for the council. Focus on security, performance, and code quality.
```

### Security-Focused Review
```
@council-security Check this SQL query builder for injection vulnerabilities: @src/db/query-builder.ts
```

### Architecture Review
```
@council-architect Is this microservice architecture appropriate for our use case? @docs/architecture.md
```

## Configuration

The council agents are configured in `.opencode/agents/`:

- `council-orchestrator.md` - Primary coordinator
- `council-architect.md` - Architecture reviewer
- `council-security.md` - Security reviewer
- `council-performance.md` - Performance reviewer
- `council-quality.md` - Quality reviewer
- `council-docs.md` - Documentation reviewer

You can customize each agent's behavior by editing these files.

## Notes

- Council members are subagents (except orchestrator) and cannot edit files by default
- The orchestrator asks for permission before making edits
- All council members provide structured feedback with severity/priority levels
- Multiple council members can be invoked in parallel for faster reviews
