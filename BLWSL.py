# banner of wsl 
# creacion de un usuario
from settings.LoginSettings import LoginSettings,User,settings
from settings.Merger import save_settings
from dotenv import load_dotenv,dotenv_values
from pydantic import SecretBytes
from settings import SL
from os import environ
from pydantic import BaseSettings
#cn = load_dotenv(r'C:\Users\ispi2\OneDrive\Documents\projects\BLWSL\settings\login.env')

##print(cn)
#print(environ.get('LoginSettings_yuniqua'))
#yun = environ.get('LoginSettings_yuniqua')
#print(type(yun))

#print(environ)
#print(environ)
#class Login(BaseModel):
#
# 

LS = LoginSettings(save_path=r'password30.txt',user=User(account_id=1,name='yuniqua',password=b'hello world11',scrypt_level_security=1,save_path=r'password.txt'))
save_settings(LS,distinct='_' + LS.user.name,format='env',perm='a')


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
