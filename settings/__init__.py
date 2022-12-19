from pydantic import BaseModel
from os import getcwd
from os.path import join
PATH = join(getcwd(),'settings',r'levels.json')
PATH_LOGIN = join(getcwd(),'settings','login.env')
ACTIVE_USERS = join(getcwd(),'settings','active.json')