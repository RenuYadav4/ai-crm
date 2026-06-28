from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router
from core.config import settings
from core.logging import configure_logging


def create_app() -> FastAPI:
    configure_logging()

    app = FastAPI(
        title=settings.PROJECT_NAME,
        version="0.1.0",
        description="AI-first CRM backend API scaffold.",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.router.routes.extend(router.routes)

    return app
