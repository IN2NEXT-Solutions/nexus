# Nexus Backend

The backend foundation for IN2NEXT Nexus.

This package provides the initial FastAPI application structure, API versioning, configuration, structured logging, error handling, health checks, and automated tests.

## Stack

- Python 3.12+
- FastAPI
- Uvicorn
- Pydantic Settings
- Pytest
- HTTPX

## Structure

```text
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── errors.py
│   │   └── logging.py
│   └── api/
│       ├── __init__.py
│       └── v1/
│           ├── __init__.py
│           ├── router.py
│           └── health.py
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   └── test_errors.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Local Setup

From the repository root:

```bash
cd backend
python -m venv .venv
```

Activate the environment.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the local environment file:

```bash
cp .env.example .env
```

On Windows, copy `.env.example` to `.env` manually if `cp` is unavailable.

## Run the API

```bash
uvicorn app.main:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

OpenAPI documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

## Health Endpoint

The initial health endpoint is:

```text
GET /api/v1/health
```

Example:

```bash
curl http://127.0.0.1:8000/api/v1/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "nexus-backend",
  "version": "0.1.0"
}
```

## API Versioning

Application APIs are versioned under:

```text
/api/v1/
```

Future incompatible API contracts may introduce:

```text
/api/v2/
```

Versioning should be used for public compatibility boundaries rather than for every internal change.

## Configuration

Configuration is loaded from environment variables using Pydantic Settings.

Important variables are documented in:

```text
.env.example
```

Never commit real secrets.

## Logging

The backend uses standard Python logging with a consistent format.

Application logs should:

- Be useful for debugging.
- Avoid secrets.
- Avoid unnecessary personal data.
- Include meaningful context.
- Support future structured logging and centralized observability.

## Error Handling

The application provides a consistent JSON response for expected application errors.

Example:

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "The requested resource was not found.",
    "request_id": "..."
  }
}
```

Unexpected errors are handled by the global exception handler and should not expose internal implementation details.

## Testing

Run:

```bash
pytest
```

The test suite currently validates:

- Health endpoint
- API versioning
- Error response behavior

## Development Principles

- Keep modules focused.
- Validate inputs at boundaries.
- Keep secrets out of source control.
- Prefer explicit dependencies.
- Add tests for new behavior.
- Keep API contracts documented.
- Avoid premature microservices.
- Follow the project's security policy.

See the repository-level `SECURITY.md` and `CONTRIBUTING.md`.

## Next Backend Milestones

The foundation is intentionally small.

Planned next steps include:

1. Database integration.
2. Dependency injection patterns.
3. Authentication.
4. Authorization.
5. User and organization models.
6. Project APIs.
7. Repository/service boundaries.
8. Background jobs.
9. Observability.
10. Integration testing.
