# XXX: ES FEISIMO CORREGIR ESTO FUNCIONA PERO ... 
#from pydantic import BaseSettings
#from .Merger import saveActiveUsers
#from . import PATH_LOGIN
#from dotenv import load_dotenv
#load_dotenv('login.env')
#config_dct = {
#            'env_file':
#                r'C:\Users\ispi2\OneDrive\Documents\projects\BLWSL\settings\login.env',
#            'env_prefix':
#                'LOGINSETTINGS_'
#        }
#active_users = ['yuniqua','tom']
#config_code =f"""
#@classmethod
#def parse_env_var(cls,field_name:str,raw_val:str):
#    from json import loads
#    if field_name in {active_users}:
#        try:
#            res = loads(raw_val)
#        except:
#            raise NameError(' no se puede decodificar el formato json')
#        return res
#    return loads(raw_val)
#"""
#exec(config_code,config_dct)
#dct_users ={
#         'Config':
#         type('Config',(object,),config_dct)
#    }
#users = ''.join(x + ':dict[str,str | dict[str,str | int]]\n' for x in ['yuniqua','tom'])
#code = f"""
#{users}
#"""
#exec(code,dct_users)
#se = type('settings',
#     (BaseSettings,)
#     ,
#     dct_users
#)
#print(se().dict())
##print(se.Config.parse_env_var('yuniqua','{"path":"abso"}'))
#
#
#class Config:
#    __active_users = saveActiveUsers().active_users
#    env_prefix = 'LOGINSETTINGS_'
#    env_file = PATH_LOGIN
#    @classmethod
#    def parse_env_var(cls,field_name:str,raw_val:str):
#        if field_name in cls.__active_users:
#            try:
#                res = cls.json_loads(raw_val)
#            except:
#                raise NameError(' no se puede decodificar el formato json')
#            return res
#        return cls.json_loads(raw_val)
#def createSettingsLoader() -> type:
#    
#    dct_users ={
#        'Config':Config
#        }
#    users = ''.join(x + ':dict[str,str | dict[str,str | int]]\n' for x in saveActiveUsers().active_users)
#    code = f"""
#{users}
#    """
#    exec(code,dct_users)
#    se = type('settings',
#         (BaseSettings,)
#         ,
#         dct_users
#    )
#    return se

"""from asciimatics.effects import RandomNoise
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys


def demo(screen):
    effects = [
        RandomNoise(screen,
                    signal=Rainbow(screen,
                                   FigletText("ASCIIMATICS")))
    ]
    screen.play([Scene(effects, -1)], stop_on_resize=True)


while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass"""
