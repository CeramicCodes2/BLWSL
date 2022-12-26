# BLWSL

    blwsl es un gestor de contrase;as y banner 
    para wsl,linux,termux y powershell puedes
    crear usuarios y guardar tus contrase;as en un sitio seguro

para usarlo debes completar una serie de pasos:

# creacion de niveles de seguridad
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
# resetear las sequencias
```py
m.resetAllSequences()
```

> BLSWL provee de un sistema de logeo usando scrypt para mayor seguridad 
> debido a ello tiene que ser prudente al colocar los niveles de seguridad
> los parametros recomendados son como en el ejemplo 

### proximas caracteristicas:

colocar anotaciones
guardar contrase;as XD
se adisionara la posivilidad de transferir archivos entre multiples dispositivos
pertenencia a gladios!

## POR HACER
* A;ADIR INSTALADOR PARA MAC WINDOWS Y LINUX
## EN PROCESO
* A;ADIR FOTO DE PERFIL PARA LOS USUSARIOS

## HECHO 
* ELIMINAR RUTAS QUE AFECTAN EL FUNCIONAMIENTO EN LINUX
