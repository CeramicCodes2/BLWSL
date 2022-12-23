from json import loads,dumps,JSONDecodeError
from hashlib import scrypt
from . import PATH,ACTIVE_USERS
from os.path import isfile
class save_settings:
    def __init__(self,dataType,distinct='',format='json',operation='w',perm='w',exclude={'user':{'password'},'path':True}) -> None:
        '''
        distinct -> un campo que distinguira uno de otra
        configuracion
        '''
        self.exclude = exclude
        self.perm = perm 
        self.distinct = distinct
        self.dataType = dataType
        self.data:str = self.dataType.json(exclude=self.exclude)
        if format =='json':
            self.save_json()
        elif operation != 'u':
            self.save()
    def save_json(self):
        with open(self.dataType.path,self.perm) as wf:
            # eliminamos el path del esquema
            wf.write(self.data)
    def save(self):
        with open(self.dataType.path,self.perm) as wf:
            # eliminamos el path del esquema
            wf.write(f'{self.dataType.__repr_name__()}{self.distinct}={self.data}\n')
    def update(self,line:int):
        with open(self.dataType.path,self.perm) as wf:
            wf.seek(0)
            buff = wf.readlines()
            for x,y in enumerate(buff):
                if x == (line - 1):
                    buff[x] = f'LoginSettings{self.distinct}={self.data}\n'
            wf.seek(0)
            wf.writelines(buff)
        
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
    def comprobateFile(self,raiseError=True) -> None | bool:
        if not(isfile(ACTIVE_USERS)):
            if raiseError:
                raise NameError('NO EXISTE EL ARCHIVO DE USUARIOS ACTIVOS')
                # si raiseError es false no se levantara una excepcion solo false
            else:
                return False
    @property
    def active_users(self) -> list[str]:
        '''
        read active users
        '''
        with open(ACTIVE_USERS,'r') as rdf: 
            try:
                au = loads(rdf.read())
            except JSONDecodeError:
                au = {}
            self.__active_users = au
            
        return au
            
    @active_users.setter
    def active_users(self,user:dict[str,int]) -> None:
        '''
        append active users
        user,account_id:int
        {'ivan':1}
        '''
        # self.comprobateFile() no necesario 
        with open(ACTIVE_USERS,'r+') as rdf:
            if self.comprobateFile(raiseError=False):
                au:dict[str,int] = {}# se crea una lista vacia
            else:
                rdf.seek(0)
                try:
                    au:dict[str,int] = loads(rdf.read())
                except JSONDecodeError:
                    au = {}
            rdf.seek(0)# me muevo a la posicion 0 para
            # sobre escribir todos los datos
            au.update(user)
            #print(au)
            rdf.write(dumps(au))
    @active_users.deleter
    def active_users(self):
        with open(ACTIVE_USERS,'w') as wf:
            wf.write('')
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
        return str(self.__account_id) + '$' + self.__salt.hex() + '$' + scrypt(self.__password,salt=self.__salt,**resp).hex() + '\n'
    def savePassword(self):
        with open(self.__path,'a') as wbf:
            wbf.write(self.kdfScrypt())
            # old save the salt the sald saves with the kd and a account id
            #self.saveSalts(account_id=self.__account_id,salt=self.__salt)
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
    def search_password(filePass:str,line_pass:str=1):
        if not(isfile(filePass)):
            raise ValueError(f'no existe el archivo {filePass}')
        else:
            with open(filePass,'r') as rb:
                if len(rb.read()) != 1:
                    rb.seek(0)
                    res = rb.readlines(line_pass)[0]
                    #XXX: SOLVE IT print(res)
            return savePassword.parsePassword(password=res)
    @staticmethod
    def parsePassword(password:str,sep:str='$') -> tuple[str | bytes | int]:
        id_pass,salt,kdf = password.split(sep)
        return int(id_pass),bytearray.fromhex(salt),kdf.replace('\n','')
    @staticmethod
    def deleteAllPassowrds(FILEPASS:str):
        with open(FILEPASS,'w') as wf:
            wf.write('')