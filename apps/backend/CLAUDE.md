# CLAUDE.md (backend)

## Stack
- FastAPI
- Pydantic
- MongoDB
- Redis

## Entry
- main.py → app bootstrap
- app_backend/app.py → core app

## Folder Structure
app_backend/
- models/ → request/response schemas (Pydantic)
- routers/ → route definitions (thin)
- services/ → business logic
- utils/ → helpers
- config.py → config
- settings.py → env handling
- db.py → DB connection
- middleware.py → middleware

## Rules
- Routes = thin (no logic)
- Services = logic
- Models = strict typing
- Utils = stateless helpers

## Patterns
- 1 route file per domain
- 1 service per domain
- group by feature if large

Example:
routers/user.py
services/user.py
models/user.py

## DB
- Use central db.py
- No direct DB access in routers
- Keep queries inside services

## Validation
- Always use Pydantic models
- No raw dict inputs

## Errors
- Raise HTTPException
- Consistent error shape

## Config
- Use env vars only
- Read via settings.py

## Health
- /health must remain lightweight

## When Adding Features
1. Model
2. Service
3. Router

## Avoid
- fat routers
- circular imports
- global state

## Observability

- All errors → must be logged
- All exceptions → sent to Sentry
- Use logger.exception for failures
- Include request_id in logs

## Testing

- Every route MUST have:
  - test in tests/
  - doc in docs/
- Tests must:
  - use stubbed data
  - not depend on DB
- All tests callable via /test?route=

## Docs

- Each route → docs/<route>.md
- Must include:
  - route
  - request
  - response
  - curl
  - test curl

## Logging

- Log flow at:
  - entry
  - exit
  - error

## Ask if unclear
- data schema?
- validation rules?
- async vs sync?
- DB structure?
- expected response?
- edge cases?
- failure scenarios?
