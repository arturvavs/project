from fastapi import FastAPI, Depends, HTTPException
from project.schemas import Message, PessoasList, Usuario, UsuarioLista, UsuarioPublico, PessoaFisicaPublic,PessoaFisica
from project.database import get_session
from sqlalchemy.orm import Session
from sqlalchemy import select
from project.models import PessoaFisicaDB, UsuarioDB
from http import HTTPStatus
from project.security import get_password_hash, verify_password
app = FastAPI()

@app.get('/',
    response_model=Message)
def root():
    return {'message':'Hello World2!'}

@app.get('/pessoas/', response_model=PessoasList,status_code=HTTPStatus.OK)
def obter_pessoas_fisica(session: Session=Depends(get_session)):
    db_pfs = session.scalars(select(PessoaFisicaDB))
    return {'users':db_pfs}

@app.get('/users/', response_model=UsuarioLista,status_code=HTTPStatus.OK)
def obter_usuarios(session: Session=Depends(get_session)):
    db_users = session.scalars(select(UsuarioDB))
    return {'users':db_users}

@app.get('/users/{id}', response_model=Usuario,status_code=HTTPStatus.OK)
def obter_usuario_id(id: int, session: Session=Depends(get_session)):
    usuario = session.scalar(select(UsuarioDB).where(UsuarioDB.user_id == id))
    return usuario

@app.post('/users/', response_model=Usuario, status_code=HTTPStatus.CREATED)
def registrar_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    db_user = session.scalar(select(UsuarioDB).where(UsuarioDB.nm_usuario == usuario.nm_usuario))
    if db_user:
        if db_user.nm_usuario == usuario.nm_usuario:
            print(db_user.nm_usuario)
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,detail = 'Usuário já existe em nosso banco de dados')
    db_user = UsuarioDB(
    nm_usuario=usuario.nm_usuario, ds_senha= get_password_hash(usuario.ds_senha))
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@app.post('/pessoa_fisica/',response_model=PessoaFisicaPublic, status_code=HTTPStatus.CREATED)
def registrar_pessoa_fisica(pessoa: PessoaFisica, session: Session=Depends(get_session)):
    new_pessoa = session.scalar(select(PessoaFisicaDB).where(PessoaFisicaDB.nm_usuario == pessoa.nm_usuario))
    #print(session)
    if new_pessoa:
        if new_pessoa.nm_usuario == pessoa.nm_usuario or new_pessoa.nr_cpf == pessoa.nr_cpf:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,detail='Usuário ou CPF já cadastrados!')
        
    new_pessoa = PessoaFisicaDB(
        nm_pessoa_fisica=pessoa.nm_pessoa_fisica,
        dt_nascimento=pessoa.dt_nascimento,
        ie_sexo=pessoa.ie_sexo,
        qt_idade=pessoa.qt_idade,
        nr_cpf=pessoa.nr_cpf,
        nm_usuario=pessoa.nm_usuario,
        ds_senha=get_password_hash(pessoa.ds_senha)
    )
    session.add(new_pessoa)
    session.commit()
    session.refresh(new_pessoa)
    return new_pessoa