import users
from users import receber_user, validar_user

user = receber_user()
print(validar_user(user))
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/")
# def home():
#     return {
#         id:0
#         email:"baka"
#     }
