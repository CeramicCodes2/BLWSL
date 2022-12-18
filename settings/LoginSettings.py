from . import BaseModel
from .User import User
from os import urandom
from pydantic import validator,ValidationError,BaseSettings
from .Merger import savePassword
from . import PATH_LOGIN

class LoginSettings(BaseModel):
    path:str = PATH_LOGIN
    user:User
    @validator('user')
    def save_password(cls,v):
        # make the kdf to the password if its saving a new password
        #scrypt(v,cls.salt)
        # save the salt in a dictonary
        salt = urandom(16)
        #savePassword.saveSalts(account_id=v.account_id, salt=salt)
        savePassword(plane_password=v.password.get_secret_value(),
                     level=v.scrypt_level_security,path=v.save_path,
        salt=salt,account_id=v.account_id).savePassword()
        # save the kd password
        return v
class settings(BaseSettings):
    #ALLOWED_USERS:list(str) = 
    activeusers:list[str]
    class Config:
        env_prefix = 'LOGINSETTINGS_'
        env_file = r'C:\Users\ispi2\OneDrive\Documents\projects\BLWSL\settings\login.env'
        @classmethod
        def parse_env_var(cls,field_name:str,raw_val:str):
            if field_name == 'activeusers':
                try:
                    res = cls.json_loads(raw_val)
                except:
                    raise NameError(' no se puede decodificar el formato json')
                return res
            return cls.json_loads(raw_val)