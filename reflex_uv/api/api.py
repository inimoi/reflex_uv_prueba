
import reflex as rx
from fastapi import FastAPI, status
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from ..api.auth import validate_token


from .auth import (
    Register,
    register_user,
    Token,
    login_user,
    Login,
    get_current_user
)

fastapi_app = FastAPI(title="Reflex + FastAPI API", version="3.0.0")

security = HTTPBearer()


# ==================== ENDPOINTS - AUTENTICACIÓN ====================

@fastapi_app.get("/", tags=["Root"])
async def read_root():
    """Endpoint raíz con información de la API"""
    return {
        "message": "Bienvenido a FastAPI + Supabase Auth",
        "version": "3.0.0",
        "auth_endpoints": {
            "POST /auth/register": "Registrarse",
            "POST /auth/login": "Iniciar sesión",
            "GET /auth/me": "Obtener usuario actual",
            "POST /auth/refresh": "Refrescar token",
            "POST /auth/logout": "Cerrar sesión",
            "PUT /auth/profile": "Actualizar perfil",
            "POST /auth/change-password": "Cambiar contraseña",
            "POST /auth/reset-password": "Solicitar reset de contraseña",
            "DELETE /auth/account": "Eliminar cuenta"
        }
    }

@fastapi_app.post("/auth/register", response_model=Token, status_code=status.HTTP_201_CREATED, tags=["Authentication"])
async def register(user: Register):
    """
    Registrar un nuevo usuario en Supabase
    """
    result = await register_user(user.email, user.password, user.name)
    
    return {
        "access_token": result["session"].access_token if result["session"] else None,
        "token_type": "bearer",
        "user": {
            "id": result["user"].id,
            "email": result["user"].email,
            "user_metadata": result["user"].user_metadata
        }
    }


@fastapi_app.post("/auth/login", response_model=Token, tags=["Authentication"])
async def login(credentials: Login):
    """
    Iniciar sesión con email y contraseña
    """
    result = await login_user(credentials.email, credentials.password)
    
    return {
        "access_token": result["access_token"],
        "token_type": "bearer",
        "user": {
            "id": result["user"].id,
            "email": result["user"].email,
            "user_metadata": result["user"].user_metadata
        }
    }

@fastapi_app.post("/validate-token")
async def validate_token_endpoint(
    credentials: HTTPAuthorizationCredentials = Depends(security),):

    credenciales = HTTPAuthorizationCredentials(scheme="Bearer", credentials=credentials.credentials)
    result = await validate_token(credentials=credenciales)
    
    return result


@fastapi_app.get("/auth/me", tags=["Authentication"])
async def get_profile_endpoint(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """Devuelve el perfil del usuario autenticado."""
    user = await get_current_user(credentials=credentials)
    return {
        "id": user.id,
        "email": user.email,
        "user_metadata": user.user_metadata,
    }



