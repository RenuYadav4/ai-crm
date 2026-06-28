# AI CRM Monorepo

Production-ready scaffold for an AI-first CRM. This repository contains only project setup, configuration, folder structure, and starter boilerplate. CRM features, AI workflows, and database models are intentionally not implemented yet.

## Stack

- Frontend: Next.js 15 App Router, React 19, TypeScript, Tailwind CSS, shadcn/ui, TanStack Query, React Hook Form, Zod, Zustand, ESLint, Prettier
- Backend: FastAPI, Python 3.11, SQLAlchemy 2.0, Alembic, Pydantic v2, JWT-ready auth structure, Redis, PostgreSQL

## Installation Commands

```powershell
git clone <repository-url>
cd ai-crm
```

## Dependency Installation Commands

```powershell
npm --prefix frontend install
python -m venv backend/.venv
backend/.venv/Scripts/Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
```

## Folder Creation Commands

The scaffold has already been created. To recreate the expected folders manually:

```powershell
New-Item -ItemType Directory -Force frontend/src, frontend/app/dashboard, frontend/app/contacts, frontend/app/companies, frontend/app/deals, frontend/app/activities, frontend/app/ai, frontend/app/analytics, frontend/app/upload, frontend/app/integrations, frontend/app/settings
New-Item -ItemType Directory -Force frontend/components/ui, frontend/components/forms, frontend/components/tables, frontend/components/charts, frontend/components/layouts, frontend/components/chat
New-Item -ItemType Directory -Force frontend/features/auth, frontend/features/contacts, frontend/features/companies, frontend/features/deals, frontend/features/analytics, frontend/features/ai
New-Item -ItemType Directory -Force frontend/hooks, frontend/services/api, frontend/services/auth, frontend/services/upload, frontend/lib, frontend/types, frontend/utils, frontend/constants
New-Item -ItemType Directory -Force backend/app, backend/api/auth, backend/api/contacts, backend/api/companies, backend/api/deals, backend/api/activities, backend/api/analytics, backend/api/upload, backend/api/ai, backend/api/integrations
New-Item -ItemType Directory -Force backend/core, backend/models, backend/schemas, backend/services/contacts, backend/services/companies, backend/services/deals, backend/services/analytics, backend/services/ai, backend/services/upload, backend/repositories, backend/workers, backend/tasks, backend/ai/prompts, backend/ai/agents, backend/ai/providers, backend/migrations/versions, backend/tests
```

## Environment Setup

Copy examples before running services:

```powershell
Copy-Item .env.example .env
Copy-Item frontend/.env.example frontend/.env.local
Copy-Item backend/.env.example backend/.env
```

Required variables:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/ai_crm
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=replace-with-a-secure-secret
OPENAI_API_KEY=
ENVIRONMENT=local
```

Start local infrastructure:

```powershell
docker compose up -d postgres redis
```

## Development Run Commands

Backend:

```powershell
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Frontend:

```powershell
cd frontend
npm run dev
```

Health check:

```powershell
Invoke-RestMethod http://localhost:8000/health
```

## Alembic Commands

```powershell
cd backend
alembic revision --autogenerate -m "initial"
alembic upgrade head
```

Do not generate migrations until database models are added.
