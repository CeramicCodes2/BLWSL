# banner of wsl 
# creacion de un usuario
from settings.LoginSettings import LoginSettings,User
from pydantic import SecretBytes
#LoginSettings(save_path=r'password.txt'
#              ,user=User(account_id=1,name='blake',password=b'hello world',
#scrypt_level_security=1,save_path=r'password.txt'))


print(User(account_id=1,name='blake',password=b'hello world',scrypt_level_security=1,save_path=r'password.txt').json())

