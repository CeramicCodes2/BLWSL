from . import BaseModel
from . import PATH
from pydantic import validator,ValidationError
#https://cryptobook.nakov.com/mac-and-key-derivation/password-encryption
class Level(BaseModel):
    n:int
    r:int
    p:int
class LevelConfig(BaseModel):
    path:str = PATH
    levels:dict[int,Level]
    @validator('levels')
    def valLevels(cls,v):
        for x in v.keys():
            if not(isinstance(x,int)):
                raise ValueError('the key should be a number')
        return v