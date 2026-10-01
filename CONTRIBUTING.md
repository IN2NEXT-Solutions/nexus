# CONTRIBUTING.md

# Contributing to IN2NEXT Nexus

Thank you for your interest in contributing to **IN2NEXT Nexus**.

Nexus is intended to be built by a diverse community of developers, designers, researchers, engineers, and technical contributors. Contributions of different sizes and from different disciplines are valuable.

Please read this document before opening an issue or pull request.

## Code of Conduct

All contributors are expected to follow the project's [Code of Conduct](CODE_OF_CONDUCT.md).

Participation in the Nexus community is conditional on respectful and constructive behavior.

## Ways to Contribute

You do not need to be a senior developer to contribute.

### Code

* New features
* Bug fixes
* Refactoring
* Performance improvements
* Tests
* Developer tooling
* Integrations
* APIs
* Plugins

### AI / ML / Data

* AI integrations
* Agent capabilities
* Retrieval systems
* Model adapters
* ML experiments
* Data pipelines
* Analytics
* Evaluation systems

### Design

* UX research
* UI design
* Design systems
* Accessibility
* User flows
* Prototypes
* Usability improvements

### Documentation

* Tutorials
* API documentation
* Guides
* Examples
* Architecture documentation
* Typographical corrections
* Translations

### Community

* Answering questions
* Reviewing proposals
* Testing releases
* Reproducing bugs
* Mentoring contributors
* Improving contributor experience

## Before You Start

Before starting substantial work:

1. Search existing issues and discussions.
2. Check the roadmap.
3. Look for an existing issue related to the work.
4. For major features or architectural changes, start a discussion or RFC before implementation.
5. Confirm that your proposed work aligns with the project's scope.

Avoid spending significant time implementing a feature that has not been discussed when the change could materially affect the architecture or public API.

## Good First Issues

Issues marked `good-first-issue` are intended to provide accessible entry points for new contributors.

They may include:

* Documentation
* Tests
* Small UI improvements
* Bug fixes
* Examples
* Developer-experience improvements

Maintainers may provide additional guidance on individual issues.

## Development Workflow

The normal contribution workflow is:

```text
Find or discuss work
        ↓
Fork repository
        ↓
Create branch
        ↓
Implement change
        ↓
Add/update tests
        ↓
Run local checks
        ↓
Open Pull Request
        ↓
Automated checks
        ↓
Code review
        ↓
Address feedback
        ↓
Approval
        ↓
Merge
```

## Branch Naming

Use descriptive branch names.

Recommended formats:

```text
feature/<short-description>
fix/<short-description>
docs/<short-description>
refactor/<short-description>
test/<short-description>
chore/<short-description>
security/<short-description>
```

Examples:

```text
feature/workflow-builder
fix/project-permission-check
docs/plugin-development
refactor/api-client
test/workflow-engine
```

## Commits

Write clear, concise commit messages.

Prefer:

```text
feat: add workflow trigger API
fix: prevent unauthorized project access
docs: document plugin lifecycle
test: add workflow validation tests
refactor: simplify permission resolver
```

Avoid commits such as:

```text
update
changes
final
fix
stuff
```

## Pull Requests

Every pull request should clearly explain:

* What changed
* Why the change was made
* Related issue or discussion
* How the change was tested
* Whether documentation was updated
* Whether the change introduces breaking behavior
* Any known limitations

For UI changes, include screenshots or recordings where useful.

For architectural changes, include relevant design decisions.

## Pull Request Checklist

Before requesting review, confirm:

* [ ] The change has a clear purpose.
* [ ] Existing functionality was considered.
* [ ] Tests were added or updated where appropriate.
* [ ] Documentation was updated where necessary.
* [ ] No secrets or credentials were added.
* [ ] No unrelated changes are included.
* [ ] The code passes applicable local checks.
* [ ] The pull request description is complete.
* [ ] Breaking changes are clearly identified.

## Code Review

Code review is intended to improve the project, not criticize contributors.

Reviewers should focus on:

* Correctness
* Security
* Maintainability
* Performance
* Architecture
* Accessibility
* Testing
* Documentation
* User impact

Contributors should respond to review comments constructively.

Maintainers may request changes before approving a pull request.

## Tests

Changes should include appropriate tests when practical.

The required test level depends on the change.

Examples:

* Utility function → unit test
* API endpoint → API/integration test
* UI component → component test where appropriate
* Workflow behavior → workflow/integration test
* Security-sensitive change → security-focused tests
* Bug fix → regression test where practical

## Documentation

Documentation is part of the implementation.

A feature that changes user-facing behavior should generally update the relevant documentation.

## Breaking Changes

Breaking changes require additional consideration.

For a breaking change:

1. Explain the impact.
2. Document migration requirements.
3. Update affected documentation.
4. Update the changelog.
5. Consider compatibility and deprecation strategies.
6. Obtain appropriate maintainer review.

## AI-Assisted Contributions

AI-assisted development is allowed.

However, contributors remain responsible for the changes they submit.

AI-generated or AI-assisted code must:

* Be reviewed by the contributor.
* Comply with project licensing requirements.
* Not contain confidential information.
* Not introduce known security vulnerabilities.
* Pass applicable tests and checks.
* Be understandable and maintainable by project contributors.

Using AI does not transfer responsibility for a pull request to the AI system.

## Security

Never publicly report security vulnerabilities through normal issues or discussions.

Follow [SECURITY.md](SECURITY.md).

Never commit:

* API keys
* Passwords
* Access tokens
* Private certificates
* Production credentials
* Personal confidential data

## Design Contributions

Designers are first-class contributors.

Design work may include:

* User flows
* Wireframes
* High-fidelity designs
* Component specifications
* Accessibility improvements
* Design-system proposals
* UX research

Design contributions should explain the problem being solved and, where applicable, provide implementation guidance.

## Robotics and Physical Systems

Future robotics and physical-device integrations require additional safety considerations.

Contributors must not introduce functionality that can cause physical actions without appropriate authorization, validation, safety controls, and documentation.

## Maintainer Review

Maintainers may:

* Request changes
* Close duplicate issues
* Redirect discussions
* Reject changes that do not align with project goals
* Request an RFC
* Defer work to a future Series

A rejected pull request does not mean the contributor is unwelcome. Contributors are encouraged to discuss the reasoning and propose alternatives.

## Becoming a Maintainer

Maintainer responsibilities are earned through sustained contribution and trust.

Relevant factors include:

* Technical quality
* Review quality
* Reliability
* Communication
* Knowledge of project architecture
* Community behavior
* Security awareness
* Documentation and mentoring

See [GOVERNANCE.md](GOVERNANCE.md).

## Questions

For general questions, see [SUPPORT.md](SUPPORT.md).

For proposed features or architectural changes, use GitHub Discussions.

Thank you for helping build Nexus.
