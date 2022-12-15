from . import BaseModel
from pydantic import SecretBytes
from collections.abc import Iterable
from pydantic import validator,ValidationError
class User(BaseModel):
    account_id:Iterable[int] 
    name:str
    password:SecretBytes#plaine text password
    @validator('password')
    def validate_password(cls,v):
        if isinstance(v,str):
            raise ValueError('the data need to be a bytes object!')