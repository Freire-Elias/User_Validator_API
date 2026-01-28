from typing import Optional
from pydantic import BaseModel, EmailStr, Field, ValidationError
import email_validator

class User(BaseModel):
    id: Optional[int] = Field(default=0, le=500)
    email: EmailStr = Field(
        description="Email do Usuário",
        examples=["usuario@gmail.com"])
    password: str = Field(min_length=5, alias="senha")



def erro(msg):
    return f"""
\033[31mERRO: {msg}\033[m
"""

def receber_user():
    try:
        with open("Teste.json", "r") as f:
            user = f.read()
        return user
    except:
        return erro("Houve um problema ao abrir o arquivo JSON")

def validar_user(usuario):
    try:
        usuario = User.model_validate_json(receber_user())
        return usuario
    except ValidationError as e:
        return erro("Informações Inválidas")


