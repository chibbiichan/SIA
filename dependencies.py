from fastapi import Cookie, HTTPException
from jose import jwt, JWTError


AUTH_SECRET = '35554cdc34fe4a073e7e978751fba97632bea34dc004328f8306249c0128f25h'


def get_token(token: str = Cookie('token')):
    try:
        user = jwt.decode(token, AUTH_SECRET)
        if user:
            return user
    except JWTError:
        raise HTTPException(401, 'Please Login first!')
