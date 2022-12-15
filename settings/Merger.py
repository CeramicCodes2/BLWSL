from json import loads
from os import urandom
from hashlib import scrypt
from . import PATH
class save_settings:
    def __init__(self,dataType) -> None:
        self.dataType = dataType
        self.data:str = self.dataType.json()
        self.save()
    def save(self):
        with open(self.dataType.path,'w') as wf:
            # eliminamos el path del esquema
            wf.write(self.data)
    @staticmethod
    def loads(filename,format='json',perm='r') ->dict:
        with open(filename,perm) as rddata:
            res  = rddata.read()
        if format == 'json':
            return loads(res)
        elif format == 'txt':
            return res
        elif format == 'binary':
            return res
class savePassword:
    def __init__(self,plane_password:bytes,level:int,path:str) -> None:
        self.__password = plane_password
        self.__level = level
        self.__levels = save_settings.loads(PATH)['levels']
        self.__path = path
    def kdfScrypt(self) -> bytes:
        resp = self.__levels.get(str(self.__level),None)
        if not(resp):
            raise ValueError('Level security not in Key Dict FATAL ERROR !')
        return scrypt(self.__password,**resp)
    def savePassword(self):
        with open(self.__path,'wb') as wbf:
            wbf.write(self.kdfScrypt())
    @staticmethod
    def saveSalts(account_id:int,salt:bytes,sep=':') -> None:
        with open('file_salts.conf','ab') as abf:
            abf.write(bytes(account_id) + ':' + salt)
    def search_password