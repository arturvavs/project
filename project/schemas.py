from pydantic import BaseModel, EmailStr
from datetime import datetime, date

class PessoaFisica(BaseModel):
    id: int
    nm_pessoa_fisica: str
    dt_nascimento: date
    qt_idade: int
    ie_sexo: str
    nr_cpf: str
    dt_nrec: datetime | None
    #dt_update: datetime | None
    
class Usuario(BaseModel):
    user_id: int
    nm_usuario: str
    #dt_nrec: datetime 
    ds_senha: str | None

class UsuarioLista(BaseModel):
    users: list[Usuario]

class PessoasList(BaseModel):
    users:list[PessoaFisica]

class Message(BaseModel):
    message: str