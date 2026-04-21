# CLAUDE.md (root)

## Purpose
Monorepo scaffold: FastAPI backend + Next.js web + infra via docker-compose.

## Structure
- apps/backend → FastAPI service
- apps/web → Next.js (App Router)
- docker-compose → local orchestration

## Global Rules
- Be concise. Min tokens. No fluff.
- Prefer edits over explanations.
- Show only changed code unless asked otherwise.
- No repetition of existing code unless required.
- Ask questions if ambiguity exists.

## Coding Principles
- Clear separation of concerns
- Predictable structure > cleverness
- Strong typing where possible
- Avoid over-abstraction
- Keep files small and modular

## Naming
- snake_case → backend (Python)
- camelCase → frontend (TS/JS)
- PascalCase → React components, classes

## Environment
- Use `.env.example` as reference
- Never hardcode secrets
- Respect service URLs from docker-compose

## API Contract
- Backend is source of truth
- Frontend consumes via typed calls
- Keep request/response models explicit

## When Making Changes
- Modify smallest possible surface
- Avoid breaking structure
- Maintain folder conventions
- If unclear → ask first

## When Unsure
Ask:
- expected behavior?
- data shape?
- edge cases?
- auth requirements?

Never assume.
