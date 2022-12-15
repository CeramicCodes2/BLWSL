# banner of wsl 
#from matrix3 import matrix
#from multiprocessing import Process
#from getpass import getpass
#from settings import LoginSettngs
from settings import SL
print(SL.LevelConfig(
    levels=
    {
    1:SL.Level(scrypt_n_mode=1,scrypt_r_mode=2,scrypt_p_mode=2),
    2:SL.Level(scrypt_n_mode=1,scrypt_r_mode=2,scrypt_p_mode=2),
    }
    ).json())