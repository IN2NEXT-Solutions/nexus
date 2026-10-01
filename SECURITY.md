# Security Policy

Security is a core requirement of IN2NEXT Nexus.

We take security reports seriously and appreciate responsible security research that helps protect Nexus users, contributors, and the wider open-source ecosystem.

## Supported Versions

Nexus is currently in early development. During this stage, security support is primarily focused on the latest maintained development or stable release.

| Version | Supported |
| --- | --- |
| Latest stable release | Yes |
| Main development branch | Best effort |
| Older releases | Generally no |

As the project matures, supported versions and security maintenance periods may be formally defined.

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub Issues, Discussions, pull requests, or social media.**

Security vulnerabilities should be reported privately through GitHub's private vulnerability reporting mechanism when it is enabled for the repository.

If private vulnerability reporting is not available, contact the security maintainers through the security contact published by IN2NEXT Solutions.

A useful security report should include:

- A clear description of the vulnerability.
- The affected component.
- The affected version, release, or commit.
- Steps required to reproduce the issue.
- A proof of concept, where appropriate.
- Potential security impact.
- Suggested mitigation, if known.

Please do not include unnecessary personal information or unrelated confidential information.

## What Happens After a Report

After receiving a security report, the maintainers will make reasonable efforts to:

1. Acknowledge the report.
2. Validate and investigate the issue.
3. Determine the affected components and versions.
4. Assess severity and potential impact.
5. Develop or coordinate an appropriate fix.
6. Test the proposed mitigation.
7. Coordinate disclosure where appropriate.
8. Publish relevant security information when appropriate.

Response times may vary depending on severity, complexity, available information, and maintainer availability.

## Responsible Disclosure

We ask security researchers to allow reasonable time for investigation and remediation before publicly disclosing technical details.

Coordinated disclosure helps protect users who have not yet had an opportunity to update.

Security researchers are encouraged to provide sufficient technical information for maintainers to reproduce and understand the vulnerability.

## Security-Sensitive Information

Never publish the following information in public issues, pull requests, discussions, or documentation:

- Passwords
- API keys
- Access tokens
- Private keys
- Authentication credentials
- Production database credentials
- Cloud credentials
- Private certificates
- Personal confidential information
- Unreleased security research
- Internal infrastructure credentials

If a secret is accidentally committed to the repository, assume that it has been compromised.

Deleting the file from the latest commit is not sufficient because the secret may remain in Git history, forks, caches, logs, or other locations.

Affected credentials should be revoked and rotated immediately.

## AI Security

Nexus may integrate artificial intelligence and machine-learning systems.

AI-related security risks may include:

- Prompt injection
- Indirect prompt injection
- Unauthorized tool execution
- Excessive agent permissions
- Sensitive-data leakage
- Retrieval poisoning
- Unsafe model-generated actions
- Insecure model integrations
- Improper trust in model output
- Inadequate human approval mechanisms

AI-generated output must not automatically be treated as trusted or authoritative.

Systems that allow AI to perform consequential actions should use appropriate authentication, authorization, validation, permission boundaries, logging, and human approval mechanisms.

## Automation Security

Automation workflows can potentially execute actions across external systems.

Contributors should consider:

- Authentication
- Authorization
- Least-privilege access
- Input validation
- Output validation
- Rate limiting
- Audit logging
- Failure handling
- Retry behavior
- Permission boundaries

Automation should not provide broader privileges than required for its intended purpose.

## Robotics and Physical Systems

Future Nexus integrations may support robotics, IoT devices, edge systems, or other physical systems.

Physical actions require additional safety considerations.

Software should not assume that an AI-generated instruction, external event, sensor value, or workflow action is automatically safe to execute on a physical device.

Where applicable, physical-device integrations should include:

- Authentication
- Authorization
- Input validation
- Device-state validation
- Safety limits
- Permission boundaries
- Failure handling
- Emergency controls
- Appropriate human approval

## Dependency and Supply-Chain Security

Nexus will use appropriate security practices for project dependencies and the software supply chain.

These may include:

- Dependency vulnerability monitoring
- Automated dependency updates
- Dependency review
- Secret detection
- Static analysis
- Code scanning
- Secure CI/CD practices
- Release integrity controls

Contributors should avoid introducing unnecessary dependencies and should consider the maintenance and security implications of new dependencies.

## Security Development Practices

Security should be considered throughout the development lifecycle.

Contributors are encouraged to:

- Validate untrusted input.
- Follow least-privilege principles.
- Avoid hard-coded credentials.
- Handle authentication and authorization explicitly.
- Write security-focused tests for sensitive functionality.
- Review dependencies before introducing them.
- Avoid exposing sensitive information in logs.
- Document security-sensitive behavior.
- Consider abuse cases during feature design.

## Security Issues in Pull Requests

If a pull request contains information that exposes a previously unknown vulnerability, do not continue discussing sensitive technical details publicly.

Contact the security maintainers privately and allow the issue to be handled through the security process.

## Security Advisories

When appropriate, IN2NEXT Solutions may publish a GitHub security advisory describing:

- Affected versions
- Severity
- Impact
- Mitigation
- Fixed versions
- Upgrade recommendations

Disclosure decisions will consider user safety, exploitability, availability of fixes, and responsible disclosure practices.

## Security Acknowledgements

We appreciate responsible security researchers and contributors who help improve Nexus security.

Where appropriate and with permission, contributors who responsibly report security vulnerabilities may be acknowledged in security advisories or project documentation.

## Policy Changes

This security policy may evolve as Nexus grows.

Changes may be made to improve:

- Vulnerability response
- Security reporting
- Supported versions
- Disclosure practices
- Development security
- Supply-chain security

Significant changes will be documented in the repository.

## Contact

For security reports, use the repository's private vulnerability reporting mechanism when available.

For general project support, see [SUPPORT.md](SUPPORT.md).

For contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).
