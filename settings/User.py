from . import BaseModel
from pydantic import SecretBytes
from pydantic import validator,ValidationError
from .Merger import save_settings
class User(BaseModel):
    account_id:int
    name:str
    password:SecretBytes#plaine text password
    scrypt_level_security:int
    __levels = save_settings.loads('levels.json')['levels']
    @validator('password')
    def validate_password(cls,v):
        if isinstance(v,str):
            raise ValueError('the data need to be a bytes object!')
    @validator('scrypt_level_security')
    def comp(cls,v):
        if not(cls.__levels.get(str(v))):
            raise ValueError('level not in levels dictonary! \n blast them ... ')