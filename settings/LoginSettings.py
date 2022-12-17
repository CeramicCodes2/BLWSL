from . import BaseModel
from .User import User
from os import urandom
from pydantic import validator,ValidationError
from .Merger import savePassword
from . import PATH_LOGIN
from pydantic import BaseSettings
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
class LoadLoginSettings(BaseSettings):
    login:LoginSettings
    class Config:
        env_file= PATH_LOGIN