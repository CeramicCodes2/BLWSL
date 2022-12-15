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
    path=r'D:\scripts\python\BLWSL\settings\test.json',
    levels=
    {
    1:SL.Level(scrypt_n_mode=1,scrypt_r_mode=2,scrypt_p_mode=2),
    2:SL.Level(scrypt_n_mode=1,scrypt_r_mode=2,scrypt_p_mode=2),
    }
    ))
ss.save()
```
