from pwdlib import PasswordHash
import jwt
from jwt import encode
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


pwd_context = PasswordHash.recommended()

SECRET_KEY = '@A1996avs#'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE = 30

def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_acess_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(minutes=ACCESS_TOKEN_EXPIRE) #Adiciona um tempo de 30 minutos de expiração do Token
    to_encode.update({'exp':expire})
    encoded_jwt = encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt