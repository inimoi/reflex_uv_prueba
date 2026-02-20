from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from supabase import create_client, Client
from pydantic import BaseModel, EmailStr
import os
from dotenv import load_dotenv

load_dotenv()

# Crear cliente de Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Esquema de seguridad
security = HTTPBearer()

# ==================== MODELOS ====================

class Register(BaseModel):
    email: EmailStr
    password: str
    name: str = None

class Login(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    user: dict

class UserProfile(BaseModel):
    id: str
    email: str
    user_metadata: dict = None
    
    class Config:
        from_attributes = True

# ==================== FUNCIONES DE AUTENTICACIÓN ====================

async def register_user(email: str, password: str, name: str = None) -> dict:
    """
    Registrar un nuevo usuario en Supabase Auth
    """
    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password,
            "options": {
                "data": {
                    "name": name or email.split("@")[0],
                    "email": email
                }
            }
        })
        
        if response.user:
            return {
                "user": response.user,
                "session": response.session
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error al registrar el usuario"
            )
    
    except Exception as e:
        error_message = str(e)
        if "already registered" in error_message or "User already exists" in error_message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya está registrado"
            )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {error_message}"
        )
    


async def login_user(email: str, password: str) -> dict:
    """
    Iniciar sesión en Supabase Auth
    """
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        
        if response.session:
            return {
                "user": response.user,
                "session": response.session,
                "access_token": response.session.access_token
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email o contraseña incorrectos"
            )
    
    except Exception as e:
        error_message = str(e)
        if "Invalid login credentials" in error_message:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email o contraseña incorrectos"
            )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {error_message}")

