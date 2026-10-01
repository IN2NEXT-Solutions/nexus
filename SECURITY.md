# Security Policy

Security is a core requirement of IN2NEXT Nexus.

Because Nexus is intended to support collaboration, automation, AI, data, integrations, and potentially physical intelligent systems, security must be considered throughout development and deployment.

## Supported Versions

As the project develops, security support will generally focus on:

| Version / Branch | Security Support |
|---|---|
| Latest stable release | Supported |
| Main development branch | Best effort |
| Older releases | Generally not supported |

Support may vary during pre-release development.

## Reporting a Vulnerability

Please do not report security vulnerabilities through:

- Public GitHub issues
- Public pull requests
- Public discussions
- Social media
- Public chat channels

Use GitHub's private vulnerability reporting/security advisory mechanism when available.

If private reporting is not available, use the security contact documented by the project maintainers.

## What to Include

A useful report should include:

- Description of the vulnerability.
- Affected component.
- Affected version or commit.
- Steps to reproduce.
- Proof of concept where appropriate.
- Potential impact.
- Suggested mitigation if known.

Please avoid including unnecessary personal or confidential information.

## Responsible Disclosure

Security researchers are encouraged to provide maintainers reasonable time to investigate and address vulnerabilities before public disclosure.

The project will aim to:

1. Acknowledge the report.
2. Validate the issue.
3. Assess severity and impact.
4. Develop a mitigation.
5. Coordinate disclosure where appropriate.
6. Publish relevant security information.

## Secrets and Credentials

Never commit:

- Passwords
- API keys
- Private keys
- Access tokens
- Cloud credentials
- Database credentials
- Production secrets

Use appropriate secret-management mechanisms for development and deployment.

## AI Security

AI-related systems may introduce risks including:

- Prompt injection
- Tool misuse
- Data leakage
- Excessive permissions
- Retrieval poisoning
- Unsafe autonomous actions
- Model manipulation
- Insecure model integrations

AI features should use least privilege, validation, appropriate boundaries, logging, and human oversight where necessary.

## Automation Security

Automation systems should be designed to prevent unintended actions.

Important controls may include:

- Permission boundaries
- Explicit action scopes
- Authentication
- Authorization
- Input validation
- Rate limits
- Audit logs
- Human approval
- Failure handling
- Safe defaults

## Robotics and Physical Systems

Systems interacting with physical environments require additional safety considerations.

Software should not assume that an automated action is harmless merely because it is technically valid.

Robotics-related systems should consider:

- Emergency stop mechanisms
- Human override
- Physical constraints
- Sensor failures
- Communication failures
- Safe fallback behavior
- Testing environments
- Deployment boundaries

## Dependencies and Supply Chain

Dependencies should be:

- Kept reasonably current.
- Reviewed for security issues.
- Pinned or constrained where appropriate.
- Audited where practical.
- Removed when unnecessary.

Build and deployment workflows should follow least-privilege principles.

## Secure Development

Contributors should consider security during:

- Architecture design
- API development
- Authentication
- Authorization
- Data handling
- Dependency selection
- CI/CD
- Infrastructure
- Logging
- AI integration
- Automation
- Deployment

## Security Advisories

Confirmed vulnerabilities may be documented through GitHub Security Advisories or other appropriate channels.

Disclosure details should balance transparency with user safety.

## Acknowledgements

The project may acknowledge security researchers who responsibly report vulnerabilities, subject to their preference.

## Policy Changes

This policy may evolve as Nexus grows.

Security requirements for future AI, automation, cloud, IoT, and robotics components may require additional controls.

## Related Documentation

- [`CONTRIBUTING.md`](CONTRIBUTING.md)
- [`GOVERNANCE.md`](GOVERNANCE.md)
- [`SUPPORT.md`](SUPPORT.md)
