from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional

class PessoaFisica(BaseModel):
    id: int
    nm_pessoa_fisica: str
    dt_nascimento: date
    qt_idade: int
    ie_sexo: str
    nr_cpf: str
    nm_usuario: str
    ds_senha: str
    dt_nrec: datetime 
    dt_updated: datetime

class PessoaFisicaPublic(BaseModel):
    id: int
    nm_pessoa_fisica: str
    dt_nascimento: date
    qt_idade: int
    ie_sexo: str
    nr_cpf: str
    nm_usuario: str
    
class Usuario(BaseModel):
    nm_usuario: str 
    ds_senha: str

class UsuarioUpdate(BaseModel):
    nm_usuario: Optional[str] = None
    ds_senha: Optional[str] = None
    #dt_updated: Optional[datetime] = None

class UsuarioPublico(BaseModel):
    user_id: int
    nm_usuario: str 

class UsuarioLista(BaseModel):
    users: list[UsuarioPublico]

class PessoasList(BaseModel):
    users:list[PessoaFisicaPublic]

class Message(BaseModel):
    message: str