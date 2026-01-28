from users import *
from fastapi import FastAPI

#Rota de verificação de dados
app = FastAPI()

@app.post("/login")
def login(dados: User):
    return {"Válido": True}

