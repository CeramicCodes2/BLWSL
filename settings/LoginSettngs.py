from . import BaseModel
from .User import User
from pydantic import validator,ValidationError
from pydantic import types as pdType
from . import Merger
class LoginSettings(BaseModel):
    save_path:pdType.FilePath
    user:User
    scrypt_level_security:int
    __levels = Merger.loads('levels.json')
    @validator('scrypt_level_security')
    def comp(cls,v):
        if not(cls.__levels.get(v)):
            raise ValueError('level not in levels dictonary! \n blast them ... ')
    @validator('User')
    def save_password(cls,v):
        # make the kdf to the password if its saving a new password
        #scrypt(v,cls.salt)
        # save the salt in a dictonary
        print(v.password)
        #Merger.save_password(v.password)
        
        #Merger.save_settings.saveSalts(cls.account_id,salt=cls.__salt)
        # save the kd password
        return v
print(LoginSettings(name='blake',password=b'Hello world'))
