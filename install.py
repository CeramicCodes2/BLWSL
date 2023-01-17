# install BLWSL
#from subprocess import Popen
from sys import platform
from os.path import isfile,join
from os import getuid,getcwd
import ctypes
class Install:
    def __init__(self):
        self.__workPath = join(getcwd(),'')
    def is_admin(self):
        is_admin = False
        try:
            is_admin = getuid() == 0
            # linux comprobamos si somos administradores si getuid() == 0 entonces estamos usando el ususario root 
            # si suelta el error AttributeError causado por ejecutarse la funcion getuid en windows 
            # se atrapara la excepcion y se preguntara si somos administradores usando la API de windows
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin
    def raiseOnAdmin(self):
        '''
        comprueba si somos administradores, si no lo somos lanzara un error
        '''
        if not(self.is_admin()):
            raise NameError('No se tienen permisos de administrador para ejecutar esta operacion \n Error.')
class Win32:
    def __init__(self):
        Install().raiseOnAdmin()
        
         
        
        
class Linux:
    def __init__(self):
        Install().raiseOnAdmin()
        # escribiremos al final del bashrc una linea para ejecutar el banner 
        self._BASHRC = join('~','./bashrc')
        if not(isfile(self.BASHRC)):
            raise NameError('[-] UBCF -> UNIKOWN UBICATION OF BASHRC')
        self.svCopy()
        self.BASHRC = f'python {join(getcwd(),"BLWSL.py")}'# escribimos el archivo del bashrc
    @property
    def BASHRC(self):
        '''getter'''
        with open(self._BASHRC,'r') as rds:
            return rds.read()
    @BASHRC.setter
    def BASHRC(self,arg:str):
        ''' write data in the bashrc file'''
        with open(self._BASHRC,'a') as fle:
            fle.write(arg)
    @BASHRC.deleter
    def BASHRC(self):
        ''' restauramos a la forma original '''
        with open(self._BASHRC + 'cpy','r') as rds:
            with open(self._BASHRC,'w') as wbf:
                wbf.write(rds.read())
    def svCopy(self):
        ''' guarda una copia del bashrc '''
        with open(self._BASHRC,'r') as rds:
            with open(self._BASHRC + 'cpy','r') as wdf:
                wdf.write(rds.read())
            
        
class Mac:
    pass

def main(platform=platform):
    match platform:
        case 'win32':
            return Win32()
        case ('linux' | 'linux2'):
            return Linux()
        case platform if 'os' in platform:
            return Mac()
if __name__ == '__main__':
    main()

