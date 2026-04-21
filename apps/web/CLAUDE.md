# CLAUDE.md (web)

## Stack
- Next.js 16 (App Router)
- MUI
- next-auth + Keycloak

## Structure
app/
- layout.tsx → root layout
- theme.tsx → MUI theme
- (protected)/ → authenticated pages

components/
- commons/ → reusable primitives
- layout/ → composed UI blocks

types/
- shared TS types

utils/
- helpers (api, etc.)

## Rules
- All UI → components/
- No logic inside pages
- Pages = composition only

## Components
commons/
- buttons, inputs, cards
- highly reusable
- no business logic

layout/
- built from commons
- page-level sections

## Styling
- Use MUI theme only
- No inline styles unless necessary
- Respect theme tokens

## Auth
- Use next-auth session
- Always send accessToken to backend

## API Calls
- Centralize in utils/api.tsx
- No raw fetch in components
- Always attach Authorization header

## Data Flow
- Server → fetch if possible
- Client → only when needed

## Types
- Define all API contracts in /types
- No implicit any

## Routing
- All protected routes inside (protected)/
- Use layout.tsx for guards

## Avoid
- duplicate components
- mixing UI + data logic
- deep prop drilling

## When Adding UI
1. Check commons first
2. Extend if needed
3. Compose in layout/
4. Use in page

## When Unclear
Ask:
- data shape?
- SSR or CSR?
- auth required?
- reuse existing component?
