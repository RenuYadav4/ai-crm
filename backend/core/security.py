from datetime import datetime, timedelta, timezone
from typing import Any

from jose import jwt, JWTError
from passlib.context import CryptContext

from core.config import settings


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str)-> str:
    print("\n========== SECURITY ==========")
    print("[Security] Hashing password")

    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str)-> bool:
    print("\n========== SECURITY ==========")
    print("[Security] Verifying password")
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict[str, Any])->str:
    print("\n========== SECURITY ==========")
    print("[Security] Creating access token")
    payload = data.copy()

    expire = datetime.now(timezone.utc)+timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update({
        "exp":expire,
        "type":"access"
    })

    print(f"[Security] Token payload: {payload}")

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )
# -------------------------
# REFRESH TOKEN
# -------------------------

def create_refresh_token(data: dict[str, Any]) -> tuple[str, datetime]:
    print("\n========== SECURITY ==========")
    print("[Security] Creating refresh token")
    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    payload.update({
        "exp": expire,
        "type": "refresh"
    })

    print(f"[Security] Token payload: {payload}")
    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return token, expire


# -------------------------
# DECODE TOKEN
# -------------------------

def decode_token(token: str):
    print("\n========== SECURITY ==========")
    print("[Security] Decoding token")
    try:
        return jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
    except JWTError:
        return None