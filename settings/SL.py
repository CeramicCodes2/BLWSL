from . import BaseModel
from pydantic import validator,ValidationError
#https://cryptobook.nakov.com/mac-and-key-derivation/password-encryption
class Level(BaseModel):
    scrypt_n_mode:int
    scrypt_r_mode:int
    scrypt_p_mode:int
class LevelConfig(BaseModel):
    levels:dict[int,Level]
    @validator('levels')
    def valLevels(cls,v):
        for x in v.keys():
            if not(isinstance(x,int)):
                raise ValueError('the key should be a number')
        return v