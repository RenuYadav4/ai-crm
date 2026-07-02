from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.organization import router as organization_router

def create_app():
    app = FastAPI()

    app.include_router(auth_router)
    app.include_router(organization_router)

    return app