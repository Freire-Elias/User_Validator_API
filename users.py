from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator
import re
import email_validator


class User(BaseModel):
    id: Optional[int] = Field(default=0, le=500)
    email: EmailStr = Field(
        description="Email do Usuário",
        examples=["usuario@gmail.com"])
    password: str = Field(
        min_length=5,
        alias="senha",
        description="""Senha do Usuário requisitos:\n
        1. 5+ Caracteres\n
        2. 1+ Caracteres especiais\n
        3. 1+ Números\n
        4. 1+ Letras maiúsculas""",
        examples=["A12345*", "Abcd1_"]
    )

    @field_validator("password")
    @classmethod
    def validar_senha(cls, sen: str):
        if not re.search("[A-Z]", sen):
            raise ValueError("Erro: É necessário pelomenos uma letra maiúscula")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", sen):
            raise ValueError("Erro: É necessário pelomenos uma caractere especial")
        if not re.search(r"\d", sen):
            raise ValueError("Erro: É necessário pelomenos um número")
        return sen

