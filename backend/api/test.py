from fastapi import APIRouter
from sqlalchemy import text
from core.database import SessionLocal

router = APIRouter()

@router.get("/db-test")
def db_test():
    db = None

    try:
        db = SessionLocal()

        result = db.execute(text("SELECT version();"))

        return {
            "status": "Database Connected Successfully",
            "postgres_version": result.scalar()
        }

    except Exception as e:
        return {
            "error": str(e)
        }

    finally:
        if db:
            db.close()