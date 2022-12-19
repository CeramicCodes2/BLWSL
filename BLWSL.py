# banner of wsl 
# creacion de un usuario
from getpass import getpass
from settings.LoginSettings import LoginSettings,User,createSettingsLoader
from settings.Merger import save_settings,saveActiveUsers,scrypt,savePassword
from dotenv import load_dotenv,dotenv_values
from secrets import compare_digest
from pydantic import SecretBytes
from settings import SL
from os import environ
from pydantic import BaseSettings
class Main:
    def __init__(self):
        self.__activeUsers = saveActiveUsers().active_users.keys()
        self.settings = createSettingsLoader()().dict()
        self.__n_cant = 3
    def login(self):
        self.__user = input('user:')
        self.__raw_pass = getpass('password:')
    def loadLoginSession(self):
        if self.__user in self.__activeUsers:
            configs = self.settings.get(self.__user)
            security_level = configs['user']['scrypt_level_security']
            # obtenemos el nivel de seguridad para ajustar los parametros de scrypt
            security_level = save_settings.loads(r'settings/levels.json')['levels'].get(str(security_level))
            if not(security_level):
                raise NameError("el nivel de seguridad asignado no es correcto ...")
            account_id,salt,kd = savePassword.search_password(filePass=configs['user']['save_path'],line_pass=int(configs['user']['account_id']))
            passTry = scrypt(password=bytes(self.__raw_pass,encoding='utf-8'),salt=bytes(salt),**security_level).hex()
            if not(compare_digest(passTry, kd)):
                print('try again! ...')
                self.__n_cant -= 1
            print('welcome !')
        else:
            print('Error unikown user ...')
    def createNewUser(self,name:str,password:str,scrypt_level_security:int,save_path:str):
        LS = LoginSettings(save_path=save_path,account_locket=False,user=User(account_id=1,name=name,password=password,scrypt_level_security=scrypt_level_security,save_path=save_path))
        save_settings(LS,distinct='_' + LS.user.name,format='env',perm='a')
        saveActiveUsers().active_users = {LS.user.name:LS.user.account_id}
    def createLevels(self):
        save_settings(
        SL.LevelConfig(levels={
        1:SL.Level(n=16384,r=8,p=1),
        2:SL.Level(n=1048576,r=8,p=1)}),format='json')
class SecureMode:
    pass
if __name__ == '__main__':
    try:
        m = Main()
        m.createNewUser(name='elisabet', password=b'hashcritic', scrypt_level_security=1, save_path=r'password.txt')
        #m.login()
        #print(saveActiveUsers().active_users)
        #m.loadLoginSession()
    except KeyboardInterrupt:
        print('starting secure mode ...')
        pass
#def createUser(username:str,password:str,scrypt_level_security:int,save_path:str):
#    LoginSettings(user=username)

#LS = LoginSettings(save_path=r'password30.txt',user=User(account_id=1,name='yuniqua',password=b'hello world11',scrypt_level_security=1,save_path=r'password.txt'))
#save_settings(LS,distinct='_' + LS.user.name,format='env',perm='a')

#settings = createSettingsLoader()
#se = settings()


#print(environ['LOGINSETTINGS_YUNIQUA'])
#print(environ)
#print(LoadLoginSettings().dict())
#load_dotenv(r'C:\Users\ispi2\OneDrive\Documents\projects\BLWSL\settings\login.env')
#print(environ['LOGINSETTINGS_ACTIVEUSERS'])
#sen = settings().dict()
#print(sen)

#
# conf = load_dotenv(r'C:\Users\ispi2\OneDrive\Documents\projects\BLWSL\settings\login.env')#

#save_settings(
#LS
#,format='env',distinct=f'_{LS.user.name}')
#"""
#save_settings(
#SL.LevelConfig(levels={
#1:SL.Level(n=16384,r=8,p=1),
#2:SL.Level(n=1048576,r=8,p=1)}),format='json')
##"""
