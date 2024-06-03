from fastapi import FastAPI
from app.auth.views import list_users, login, register
from app.auth.schemas import LoginBody, RegisterBody


def use_auth(app: FastAPI):
    app.get('/api/auth/users')(list_users)
    app.post('/api/auth/login')(login)
    app.post('/api/auth/register')(register)


__all__  = ['LoginBody', 'RegisterBody']
