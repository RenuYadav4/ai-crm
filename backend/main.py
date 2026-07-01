from app.factory import create_app

app = create_app()


@app.get("/")
def root():
    return {"message": "FastAPI running"}