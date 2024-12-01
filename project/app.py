from fastapi import FastAPI, Depends
from project.schemas import Message, PessoasList, Usuario, UsuarioLista
from project.database import get_session
from sqlalchemy.orm import Session
from sqlalchemy import select
from project.models import PessoaFisica, Usuario
from http import HTTPStatus
app = FastAPI()

@app.get('/',
    response_model=Message)
def root():
    return {'message':'Hello World2!'}

@app.get('/pessoas/', response_model=PessoasList,status_code=HTTPStatus.OK)
def get_pfs(session: Session=Depends(get_session)):
    db_pfs = session.scalars(select(PessoaFisica))
    return {'users':db_pfs}

@app.get('/users/', response_model=UsuarioLista,status_code=HTTPStatus.OK)
def get_users(session: Session=Depends(get_session)):
    db_users = session.scalars(select(Usuario))
    return {'users':db_users}