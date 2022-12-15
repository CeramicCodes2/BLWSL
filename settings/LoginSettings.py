from . import BaseModel
from .User import User
from pydantic import validator,ValidationError
from .Merger import savePassword
class LoginSettings(BaseModel):
    user:User
    @validator('user')
    def save_password(cls,v):
        # make the kdf to the password if its saving a new password
        #scrypt(v,cls.salt)
        # save the salt in a dictonary
        savePassword.saveSalts(account_id=v.account_id, salt=urandom(16))
        savePassword(plane_password=v.password, level=v.scrypt_level_security,path=v.save_path).savePassword()
        # save the kd password
        return v