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

class Main:
    def __init__(self):
        self.__activeUsers = saveActiveUsers().active_users.keys()
        self.se = createSettingsLoader()()
        self.settings = self.se.dict()
    def login(self):
        self.__user = input('user:')
        self.__raw_pass = getpass('password:')
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
    def logn(self):
            cc = 1
            while cc > 0:
                self.login()
                if self.loadLoginSession():
                    res = self.loadUserConfigs()
                    if not(res):
                        print('try again! ...')
                        cc-= 1
                    else:
                        print('welcome !')
                        exit()# enf of the program
                        break
            # in other case we lock the account
            print('too many try`s locking the account ...')
            self.lockAccount()
    def loadLoginSession(self):
        if self.__user in self.__activeUsers:
            self.configs = self.settings.get(self.__user)
            if self.configs['account_locket']:
                print('account locket ...')
                return False
            return True
        else:
            print('Error unikown user ...')
            return False
    def lockAccount(self):
            #configs['account_locket'] = True
            self.configs['account_locket'] = True
            self.configs['user']['password'] = b''# solo agregamos un campo vacio
            # no se requiere pero es mas facil que crear una clase nueva
            lg = LdLogin.parse_obj(self.configs)
            #js = dumps(self.configs)
            #print(self.settings[self.__user]['user']['account_id'])
            save_settings(lg,perm='r+',format='env',distinct='_' + lg.user.name,operation='u').update(lg.user.account_id) 
    def createNewUser(self,name:str,password:str,scrypt_level_security:int,save_path:str):
        seq = SequenceMerger.parse_file(PATH_SEQUENCES)
        LS = LoginSettings(save_path=save_path,account_locket=False,user=User(account_id=seq.sequences['SQ_ACCOUNT_ID'].nextValue,name=name,password=password,scrypt_level_security=scrypt_level_security,save_path=save_path))
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
class SecureMode:
    pass

if __name__ == '__main__':
    m = Main()
    #m.createNewUser(name, password, scrypt_level_security, save_path)