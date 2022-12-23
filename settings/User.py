from . import BaseModel
from pydantic import SecretBytes
from pydantic import validator,ValidationError
from .Merger import save_settings
#from pydantic import types as pdType
from . import PATH
class User(BaseModel):
    account_id:int
    name:str
    password:SecretBytes#plaine text password
    save_path:str
    scrypt_level_security:int
    is_admin:bool
    __levels = save_settings.loads(PATH)['levels']
    @validator('password')
    def validate_password(cls,v):
        if isinstance(v,str):
            raise ValueError('the data need to be a bytes object!')
        
        return v
    @validator('scrypt_level_security')
    def comp(cls,v):
        if not(cls.__levels.get(str(v),None)):
            raise ValueError('level not in levels dictonary! \n blast them ... ')
        return v