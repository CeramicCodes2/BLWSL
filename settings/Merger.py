from json import loads
from hashlib import scrypt
from . import PATH,ACTIVE_USERS
from os.path import isfile
class save_settings:
    def __init__(self,dataType,distinct='',format='json',perm='w') -> None:
        '''
        distinct -> un campo que distinguira uno de otra
        configuracion
        '''
        self.perm = perm 
        self.distinct = distinct
        self.dataType = dataType
        self.data:str = self.dataType.json()
        if format =='json':
            self.save_json()
        else:
            self.save()
    def save_json(self):
        with open(self.dataType.path,self.perm) as wf:
            # eliminamos el path del esquema
            wf.write(self.data)   
    def save(self):
        with open(self.dataType.path,self.perm) as wf:
            # eliminamos el path del esquema
            wf.write(f'{self.dataType.__repr_name__()}{self.distinct}={self.data}\n')
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
class saveActiveUsers:
    def __init__(self) -> None:
        self.__active_users = []
    def openActiveUsersFile(self):
        self.__awrf = open(ACTIVE_USERS,'a+')
    def __del__(self,*args,**kwargs):
        self.__awrf.close()
        
        # se cierra el archivo cuando se elimine el objeto
        # asi en lugar de estar abriendo y abriendo por cada operacion
        # solo se abre una vez
    @property
    def active_users(self):
        
        self.__active_users.append()
class savePassword:
    def __init__(self,plane_password:bytes,level:int,path:str,salt:bytes,account_id:int) -> None:
        self.__password = plane_password
        self.__level = level
        self.__levels = save_settings.loads(PATH)['levels']
        self.__path = path
        self.__salt = salt
        self.__account_id = account_id
    def kdfScrypt(self) -> bytes:
        resp = self.__levels.get(str(self.__level),None)
        if not(resp):
            raise ValueError('Level security not in Key Dict FATAL ERROR !')
        return scrypt(self.__password,salt=self.__salt,**resp)
    def savePassword(self):
        with open(self.__path,'wb') as wbf:
            wbf.write(self.kdfScrypt())
            self.saveSalts(account_id=self.__account_id,salt=self.__salt)
    @staticmethod
    def saveSalts(account_id:int,salt:bytes,sep=':') -> None:
        if not(isfile('file_salts.conf')):
            print('[-] WARNING: file_salts.conf does not exists\n [+] creating ...')
        with open('file_salts.conf','ab') as abf:
            abf.write(bytes(account_id) + b':' + salt)
    @staticmethod
    def getSalt(account_id:str)->bytes:
        '''
        method destined to return the salt
        extracted from the file_salts.conf
        '''
        if isfile('file_salts.conf'):
            with open('file_salts.conf','rb') as rbf:
                salt = rbf.readline(account_id)
                # account id corresponds to the line
            return salt
        else:
            raise NameError('ERROR file_salts.conf does not exists!')
    @staticmethod
    def search_password():
        pass