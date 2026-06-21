from fastapi import FastAPI
from api.test import router

app = FastAPI(
    title = "AI CRM API",
    version = "1.0.0",
    description = "AI first CRM backend",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "AI CRM backend running"  
    }
