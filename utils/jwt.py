import os
from datetime import datetime, timedelta, UTC
from jose import JWTError, jwt

# Clé secrète à garder privée
SECRET_KEY = os.getenv("JWT_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None)->str:
    if SECRET_KEY is None:
        raise Exception("JWT_KEY is missing")
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload["username"]
        if username is None:
            raise JWTError()
        return payload
    except JWTError:
        return None
