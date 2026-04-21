import requests
from jose import jwt
from settings import settings

JWKS_URL = f"{settings.KEYCLOAK_BASE_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/certs"
jwks = requests.get(JWKS_URL).json()


def verify_token(token: str):
    return jwt.decode(
        token,
        jwks,
        algorithms=[settings.JWT_ALGORITHM],
        audience=settings.KEYCLOAK_CLIENT_ID,
    )