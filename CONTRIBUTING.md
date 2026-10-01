# Contributing to IN2NEXT Nexus

Thank you for your interest in contributing to Nexus.

Nexus is intended to be an open-source project where people with different technical and non-technical backgrounds can collaborate.

## Ways to Contribute

You can contribute through:

- Software development
- Backend development
- Frontend development
- AI/ML
- Data science and engineering
- Automation
- DevOps and infrastructure
- Security
- UI/UX and design
- Documentation
- Testing and quality assurance
- Research
- Community support
- Project management
- Robotics, IoT, and intelligent systems

## Before You Start

Before making a significant change:

1. Read the project documentation.
2. Check existing issues and discussions.
3. Review the roadmap.
4. Search for existing work related to your idea.
5. Open an issue or discussion for large architectural changes.

Small documentation and maintenance changes can usually proceed directly through a pull request.

## Development Workflow

The preferred workflow is:

```text
Issue / Discussion
       |
       v
Create branch
       |
       v
Implement change
       |
       v
Run tests
       |
       v
Open Pull Request
       |
       v
Code review
       |
       v
Approval
       |
       v
Merge
```

## Branch Naming

Use descriptive branch names.

Recommended prefixes:

```text
feature/
fix/
docs/
refactor/
test/
chore/
security/
```

Examples:

```text
feature/user-authentication
fix/api-timeout
docs/update-architecture
refactor/workflow-engine
test/api-integration
security/harden-permissions
```

## Commits

Use clear, focused commit messages.

Recommended prefixes:

```text
feat:
fix:
docs:
test:
refactor:
chore:
security:
```

Examples:

```text
feat: add workflow execution API
fix: handle invalid authentication token
docs: update contribution guide
test: add workflow validation tests
refactor: simplify permission service
security: restrict tool execution permissions
```

Keep commits focused and avoid mixing unrelated changes.

## Pull Requests

Every pull request should:

- Explain what changed.
- Explain why the change was needed.
- Identify relevant issues.
- Include tests where appropriate.
- Update documentation when required.
- Mention breaking changes.
- Avoid unrelated modifications.
- Pass required CI checks.

## Pull Request Checklist

Before requesting review:

- [ ] The change has a clear purpose.
- [ ] Relevant documentation has been updated.
- [ ] Tests have been added or updated where appropriate.
- [ ] Existing tests pass.
- [ ] Security implications have been considered.
- [ ] No secrets or credentials are committed.
- [ ] Breaking changes are clearly documented.
- [ ] The pull request is focused and reviewable.

## Code Review

Reviewers should focus on:

- Correctness
- Security
- Maintainability
- Reliability
- Performance
- Testing
- Documentation
- API compatibility
- User impact

Review comments should be respectful, specific, and actionable.

## AI-Assisted Contributions

AI-assisted development is allowed.

Contributors remain responsible for:

- Reviewing generated code.
- Understanding the submitted changes.
- Verifying correctness.
- Checking licenses and attribution.
- Testing generated code.
- Checking for security issues.
- Avoiding confidential or private information in AI tools.

Do not submit AI-generated material that you do not have the right to contribute.

## Security Contributions

Do not disclose vulnerabilities through public issues, discussions, or pull requests.

Follow [`SECURITY.md`](SECURITY.md) for security reporting.

## Robotics and Physical Systems

Contributions involving physical systems, robotics, autonomous behavior, or hardware should consider:

- Physical safety
- Failure modes
- Human override
- Testing environments
- Deployment boundaries
- Permission controls
- Emergency procedures

## Documentation Contributions

Documentation is a first-class contribution.

Examples include:

- Tutorials
- Architecture documentation
- API documentation
- Examples
- Troubleshooting
- Guides
- Diagrams
- Installation instructions

## Becoming a Maintainer

Maintainer responsibilities are documented in [`GOVERNANCE.md`](GOVERNANCE.md).

Maintainer status is based on sustained contribution, technical understanding, responsible collaboration, and demonstrated commitment to project quality and security.

## License

By contributing, you agree that your contribution is provided under the project's applicable license and contribution terms.

See [`LICENSE`](LICENSE) and [`GOVERNANCE.md`](GOVERNANCE.md).

## Final Note

There is no single required background for contributing to Nexus.

Good documentation, thoughtful feedback, testing, design, research, and community work can be just as valuable as writing code.
