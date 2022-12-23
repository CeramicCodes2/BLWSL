# banner of wsl 
# creacion de un usuario
from getpass import getpass
from settings.LoginSettings import LoginSettings,User,createSettingsLoader,LdLogin
from settings.Merger import save_settings,saveActiveUsers,scrypt,savePassword
from dotenv import load_dotenv,dotenv_values
from secrets import compare_digest
from settings.sequences import SequenceMerger,PATH_SEQUENCES
from pydantic import SecretBytes
from settings import SL
from os import environ
from pydantic import BaseSettings
from sys import exit

class Model:
    def __init__(self,out):
        self.__activeUsers = saveActiveUsers().active_users.keys()
        self.se = createSettingsLoader()()
        self.settings = self.se.dict()
        self.out =  out
        self.isLocked = False
        self.__cc = 0
        self.__is_admin =  False
        self.__str2bool = lambda x: True if x == 'True' else False
        #self.out_secret = out_secret
        #self._in_secret = in_secret
        #self._input = input_n
    """    def login(self):
        self.__user = self._input('user:')
        self.__raw_pass = self._in_secret('password:')"""
    def getcc(self):
        return self.__cc
    def loadUserConfigs(self) -> bool:
            security_level = self.configs['user']['scrypt_level_security']
            # obtenemos el nivel de seguridad para ajustar los parametros de scrypt
            security_level = save_settings.loads(r'settings/levels.json')['levels'].get(str(security_level))
            if not(security_level):
                raise NameError("el nivel de seguridad asignado no es correcto ...")
            account_id,salt,kd = savePassword.search_password(filePass=self.configs['user']['save_path'],line_pass=int(self.configs['user']['account_id']))
            passTry = scrypt(password=bytes(self.__raw_pass,encoding='utf-8'),salt=bytes(salt),**security_level).hex()
            #passTry = self.__raw_pass
            
            return compare_digest(passTry, kd)
    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self,arg):
        self.__user = arg
    @property
    def password(self):
        return ''
    @password.setter
    def password(self,other:str):
        self.__raw_pass = other
    """    def logn(self):
            cc = 3
            while cc > 0:
                self.login()
                if self.loadLoginSession():
                    res = self.loadUserConfigs()
                    if not(res):
                        self.out('try again! ...')
                        cc-= 1
                    else:
                        self.out('welcome !')
                        exit()# enf of the program
                        break
            # in other case we lock the account
            self.out('too many try`s locking the account ...')
            self.lockAccount()"""
    def logn(self):
        #self.updateSettings()
        self.configs = self.settings.get(self.__user)
        # for each call to login will update the settings dict
        if self.__cc >= 3:
            self.out = 'too many try`s locking the account ...'
            self.lockAccount()
            self.isLocked = True
            self.__cc = 0
        if self.loadLoginSession():
            res = self.loadUserConfigs()
            if not(res):
                self.out = 'try again! ...'
                self.__cc += 1
            else:
                self.out = 'welcome !'
                return True
                #exit(0)
    def loadLoginSession(self):
        if self.__user in self.__activeUsers:
            if self.configs['account_locket']:
                self.out = 'account locket ...'
                return False
            priv = self.__str2bool(self.configs['user']['is_admin'])
            if priv:
                self.isAdmin = True
            elif not(priv):
                self.isAdmin = False
            #print(f'priv:',priv,self.configs['user']['is_admin'])
            return True
        else:
            self.out = 'Error unikown user ...'
            return False
    def lockAccount(self):
        #configs['account_locket'] = True
        self.configs['account_locket'] = True
        self.configs['user']['password'] = b''# solo agregamos un campo vacio
        # no se requiere pero es mas facil que crear una clase nueva
        lg = LdLogin.parse_obj(self.configs)
        #js = dumps(self.configs)
        #self.out(self.settings[self.__user]['user']['account_id'])
        save_settings(lg,perm='r+',format='env',distinct='_' + lg.user.name,operation='u').update(lg.user.account_id) 
    def updateSettings(self) -> None:
        """
            this mehthod will update the self.settings dict 
            from the data writed in the files
        """
        self.se:Type = createSettingsLoader()()
        self.settings:dict = self.se.dict()
        #print(self.__activeUsers)
        self.__activeUsers = saveActiveUsers().active_users.keys()
    def unlockAccount(self,name) -> bool:
        user = self.settings.get(name)
        if not(user):
            self._out = 'El ususario no existe Error ...'
            return False
        #self.configs['user']['password'] = b''
        user['user']['password'] = b''
        user['account_locket'] = False
        lg = LdLogin.parse_obj(user)
        save_settings(lg,perm='r+',format='env',distinct='_' + lg.user.name,operation='u').update(lg.user.account_id)
        self.updateSettings()
    def getAllLocketAccounts(self) -> list[str]:
        ''' return`s the users where account_locket is True '''
        return [ (x,y) for x,y in self.settings.items() if y['account_locket'] == True]
    def createNewUser(self,name:str,password:str,scrypt_level_security:int,save_path:str,is_admin:bool=False):
        seq = SequenceMerger.parse_file(PATH_SEQUENCES)
        LS = LoginSettings(save_path=save_path,account_locket=False,user=User(account_id=seq.sequences['SQ_ACCOUNT_ID'].nextValue,name=name,password=password,scrypt_level_security=scrypt_level_security,save_path=save_path,is_admin=is_admin))
        save_settings(LS,distinct='_' + LS.user.name,format='env',perm='a')
        saveActiveUsers().active_users = {LS.user.name:LS.user.account_id}
        seq.saveSequence()
    def createLevels(self):
        save_settings(
        SL.LevelConfig(levels={
        1:SL.Level(n=16384,r=8,p=1),
        2:SL.Level(n=1048576,r=8,p=1)}),format='json')
    def resetAllSequences(self):
        #m.createNewUser(name='carlos', password=b'password', scrypt_level_security=1, save_path='password.txt')
        seq = SequenceMerger.parse_file(PATH_SEQUENCES)
        for key,sequence in seq.sequences.items():
            sequence.value = 0
        seq.saveSequence()
    @property
    def isAdmin(self):
        return self.__is_admin
    @isAdmin.setter
    def isAdmin(self,other:bool):
        self.__is_admin = other
class SecureMode:
    pass

#m = Model(out=print)
#m.user = 'carlos'
#m.password = 'pepe~'
#m.logn()
#m.createNewUser(name='carlos', password=b'password', scrypt_level_security=1, save_path='password.txt')