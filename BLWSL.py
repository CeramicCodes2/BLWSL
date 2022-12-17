# banner of wsl 
# creacion de un usuario
from settings.LoginSettings import LoginSettings,User,LoadLoginSettings
from settings.Merger import save_settings
from dotenv import load_dotenv
from pydantic import SecretBytes
from settings import SL
from os import environ
#class Login(BaseModel):
LS = LoginSettings(save_path=r'password30.txt',user=User(account_id=1,name='yuniqua',password=b'hello world11',scrypt_level_security=1,save_path=r'password.txt'))
print(LoadLoginSettings().dict())

#save_settings(
#LS
#,format='env',distinct=f'_{LS.user.name}')

conf = load_dotenv(r'C:\Users\ispi2\OneDrive\Documents\projects\BLWSL\settings\login.env')#
"""save_settings(
SL.LevelConfig(levels={
1:SL.Level(n=16384,r=8,p=1),
2:SL.Level(n=1048576,r=8,p=1)}),format='json')"""
