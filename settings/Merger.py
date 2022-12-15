from json import loads
from os import urandom
from hashlib import scrypt
class save_settings:
    def __init__(self,dataType) -> None:
        self.dataType = dataType
        self.data:str = self.dataTtype.json()
        self.save()
    def save(self):
        with open(self.dataType.path,'w') as wf:
            del self.data['path']
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
    @staticmethod
    def saveSalts(account_id:int,salt:bytes,sep=':') -> None:
        with open('file_salts.conf','ab') as abf:
            abf.write(bytes(account_id) + ':' + salt)
class savePassword:
    def __init__(self,plane_password:bytes,level:int) -> None:
        self.__password = plane_password
        self.__level = level
        self.__levels = save_settings.loads('levels.json')
    def kdfScrypt(self) -> bytes:
        resp = self.__levels.get(self.__level)
        if not(resp):
            raise ValueError('Level security not in Key Dict FATAL ERROR !')
        return scrypt(self.__password,**resp)
    def savePassword(self):
        
        pass