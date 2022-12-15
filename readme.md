# BLWSL

    blwsl es un gestor de contrase;as y banner 
    para wsl puedes colorar anotanciones
    crear usuarios y guardar tus contrase;as en un sitio seguro

para usarlo debes completar una serie de pasos:

# creacion de archivo basico de configuracion
```py
from settings import SL
from settings import Merger

ss = Merger.save_settings(
SL.LevelConfig(
    path=r'D:\scripts\python\BLWSL\settings\levels.json',
    levels=
    {
    1:SL.Level(n=16384,r=8,p=1),
    2:SL.Level(n=1048576,r=8,p=1),
    }
    ))
ss.save()
```
