# banner of wsl 
# creacion de un usuario
from getpass import getpass
from settings.LoginSettings import LoginSettings,User,createSettingsLoader
from settings.Merger import save_settings
from dotenv import load_dotenv,dotenv_values
from pydantic import SecretBytes
from settings import SL
from os import environ
from pydantic import BaseSettings
class Main:
    def __init__(self):
        pass
    def login(self):
        self.__user = input('user:')
        self.__raw_pass = getpass('password:')
    def loadLoginSession(self):
        pass
    def createNewUser(self,name:str,password:str,scrypt_level_security:int,save_path:str):
        
        LS = LoginSettings(save_path=save_path,user=User(account_id=1,name=name,password=password,scrypt_level_security=scrypt_level_security,save_path=save_path))
        save_settings(LS,distinct='_' + LS.user.name,format='env',perm='a')
    def createLevels(self):
        save_settings(
        SL.LevelConfig(levels={
        1:SL.Level(n=16384,r=8,p=1),
        2:SL.Level(n=1048576,r=8,p=1)}),format='json')
if __name__ == '__main__':
    try:
        Main()
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
