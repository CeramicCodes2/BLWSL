from . import BaseModel
from .User import User
from pydantic import validator,ValidationError
from pydantic import types as pdType
from . import Merger
class LoginSettings(BaseModel):
    save_path:pdType.FilePath
    user:User
    @validator('User')
    def save_password(cls,v):
        # make the kdf to the password if its saving a new password
        #scrypt(v,cls.salt)
        # save the salt in a dictonary
        Merger.savePassword(plane_password=v.password, level=v.scrypt_level_security,path=cls.save_path)     
        #Merger.save_settings.saveSalts(cls.account_id,salt=cls.__salt)
        # save the kd password
        return v
#print(LoginSettings(save_path=r'D:\scripts\python\BLWSL\settings\hello.txt',user=User(account_id=1,name='blake12b',password='password',scrypt_level_security=1)))
