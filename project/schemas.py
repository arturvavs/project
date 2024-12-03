from pydantic import BaseModel, EmailStr
from datetime import datetime, date

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

class UsuarioPublico(BaseModel):
    user_id: int
    nm_usuario: str 

class UsuarioLista(BaseModel):
    users: list[Usuario]

class PessoasList(BaseModel):
    users:list[PessoaFisicaPublic]

class Message(BaseModel):
    message: str