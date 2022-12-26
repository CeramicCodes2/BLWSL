from Model import Model
from asciimatics.widgets import Frame,Button,Text,Layout,Divider,Widget,Label,ListBox
from asciimatics.widgets.radiobuttons import RadioButtons
from asciimatics.widgets.popupdialog import PopUpDialog
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics.effects import RandomNoise,Julia,Print
from asciimatics.renderers import ColourImageFile,FigletText
class AcountInfo(Frame):
    def __init__(self, screen,model):
        super(AcountInfo,self).__init__(
            screen,
            screen.height*2//3,
            screen.width *2// 3,
            #y=0,
            on_load=self._fill_values,
            hover_focus=True,
            title="Admin Display Infro User",
        )
        self.__str2bool = lambda x: True if x in ('True','true') else False
        self._model = model 
        self._tiName = Text(label='Name',name='name')
        self._tiLvlSec = Text(label='Level Security',name='scrypt_level_security',readonly=True)
        self._tiLock = RadioButtons(options=[('true',True),('false',False)],label='is locked',name='account_locket')#validator=self.__str2bool)
        self._tiAdmin = RadioButtons(label='is admin',name='is_admin',options=[('true',True),('false',False)])
        self._fill_values()
        self.set_theme(theme='green')
        # buttons ly2
        self._bEdit = Button(text='Edit',on_click=self._edit)
        self._bDelete = Button(text='Delete', on_click=self._delete)
        layout = Layout([10,90],fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self._tiName,1)
        layout.add_widget(Divider(draw_line=False),1)
        layout.add_widget(self._tiLvlSec,1)
        layout.add_widget(Divider(draw_line=False),1)
        layout.add_widget(self._tiLock,1)
        layout.add_widget(Divider(draw_line=False),1)
        layout.add_widget(self._tiAdmin,1)
        layout.add_widget(Divider(height=3,draw_line=False))
        ly2 = Layout([1,1,1,1])
        self.add_layout(ly2)
        ly2.add_widget(self._bEdit,0)
        #ly2.add_widget(self._bDelete,1)
        ly2.add_widget(Divider(draw_line=False,height=3))
        ly2.add_widget(Button(text='Return to Admin',on_click=self._return2Admin),2)
        ly2.add_widget(Button(text='Exit',on_click=self._exit),3)
        ly2.add_widget(Divider(draw_line=False,height=3))
        self.fix()
        self._on_pick()
    def _return2Admin(self):
        raise NextScene('AdminDisplay')
    def _fill_values(self):
        #print(self._model.userSelected)
        if self._model.userSelected != None:
            configs = self._model.userSelected
            self._tiName.value = configs['user'][self._tiName.name]
            self._tiLvlSec.value = configs['user'][self._tiLvlSec.name]
            self._tiLock.value = configs[self._tiLock.name]
            self._tiAdmin.value = configs['user'][self._tiAdmin.name]
        else:
            self._tiName.value = 'NO DATA ...'
    def _on_pick(self):
        #hasattr(obj, name)
        pass
        #print(f'fs {self._model.userSelected}')
        #self._bEdit.disabled = self._model.userSelected is None
    def _edit(self):
        self.save()
        dta = self.data
        configs = self._model.userSelected
        oldName = configs['user']['name']
        configs['user']['name'] = dta['name']
        
        configs['user']['scrypt_level_security'] = dta['scrypt_level_security']
        configs['user']['is_admin'] = dta['is_admin']
        configs['account_locket'] = dta['account_locket']
        self._model.updateUser(configs)
        if oldName != dta['name']:
            self._model.updateActiveUser(oldName, dta['name'])
            # checamos si se actualizo el nombre de ususario
        #raise NextScene('Info')
    def _delete(self):
        pass
    def _exit(self):
        raise StopApplication('req')
class AnimeGril(Print):
    def __init__(self,screen:Screen,image:str):
        super(AnimeGril,self).__init__(
            screen,

            ColourImageFile(screen, 
                            image,
                            height=screen.height,
                            uni=True,
                            dither=True,
                            fill_background=True
                            ),
            y=0,
            x=int(screen.width * 0.01),
            stop_frame=0 
            )
            
        
class UsersDisplay(Frame):
    def __init__(self, screen,model:Model):
        super(UsersDisplay,self).__init__(
            screen,
            screen.height,
            int(screen.width* 0.56),
            x=int(screen.width * 0.44),
            on_load=self._load_list
            )
        self._screen = screen
        self._model = model
        self._list_view = ListBox(
            Widget.FILL_FRAME,
            model.getAllUsers(),
            name="usersInfo",
            add_scroll_bar=True,
            on_change=self._on_pick,
            on_select=self._set_user
            )
        self._bedit = Button(text='Edit',on_click=self._edit)
        self._bduser = Button('Delete User',self._delete_user)
        self.set_theme(theme='green')
        layout = Layout([30,70],fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Label('Users:',height=3),0)
        layout.add_widget(Divider(height=2,draw_line=False),1)
        layout.add_widget(self._list_view,1)
        layout.add_widget(Divider(height=2,draw_line=False),1)
        l2 = Layout([1,1,1,1])
        self.add_layout(l2)
        l2.add_widget(self._bedit,0)
        l2.add_widget(Button('Exit',self._exit),3)
        l2.add_widget(Button('Return to admin',self._returnToAdmin),1)
        l2.add_widget(self._bduser,2)
        #self.add_layout(layout
        # )
        self.fix()
        self._on_pick()
    def _set_user(self):
        self.save()
        selection:dict[str,str] = self.data['usersInfo']
        # valor seleccionado
        self._model.userSelected = selection  
    def _delete_user(self):
        self.save()
        se:dict[str,str] = self.data['usersInfo']
        self._model.userSelected = se
        self._model.deleteUser()
        self._load_list()
        raise NextScene("UsersDisplay")
        pass
    def _exit(self):
        raise StopApplication('Stop application')
    def _returnToAdmin(self):
        raise NextScene('AdminDisplay')
    def _on_pick(self):
        self._bedit.disabled = self._list_view is None
        self._bduser.disabled = self._list_view is None
    def _load_list(self):
        self.save()
        self._list_view.options = self._model.getAllUsers()
    def _edit(self):
        self.save()
        selection:dict[str,str] = self.data['usersInfo']
        # valor seleccionado
        self._model.userSelected = selection
        raise NextScene("Info")
        
class basic(Frame):
    def __init__(self, screen:Screen,model:Model):
        super(basic,self).__init__(
            screen,
            screen.height,
            screen.width // 3,
            #y=0,
            x=0,
            hover_focus=True,
            title="Admin Display 2",
            
        )
        self._screen = screen
        self._model = model
        # 0 1 and 3 0 for none
        self.set_theme(theme='green')
        l = Layout([100])
        self.add_layout(l)
        l.add_widget(Button(text='Delete all users',on_click=self._delete))
        l.add_widget(Button(text='Restart sequences',on_click=self._restart_seq))
        
        self.fix()
    def _delete(self):
        self._model.deleteAllUsers()
        #self._model.resetAllSequences()
        
        raise StopApplication('requested !')
    def _restart_seq(self):
        self._model.resetAllSequences()
        raise StopApplication('requested !')
class AdminDisplay(Frame):
    def __init__(self, screen:Screen,model:Model):
        super(AdminDisplay,self).__init__(
            screen,
            height=screen.height,
            width=screen.width * 2 // 3,
            #y=int(screen.height // 3),
            x=(screen.width // 3),
            hover_focus=True,
            title="Admin Display",
            on_load=self._reloadList
        )
        self._model = model
        #model.updateSettings()
        self._list_view = ListBox(
            Widget.FILL_FRAME,
            model.getAllLocketAccounts(),
            name="locketUsers",
            add_scroll_bar=True,
            on_change=self._on_pick,
            on_select=self._edit)
        self.set_theme(theme='green')
        self._edit_button = Button(text='Enable User',on_click=self._edit)
        layoutContent = Layout([100],fill_frame=True)
        self.add_layout(layoutContent)
        layoutContent.add_widget(Label('Locket users:'))
        layoutContent.add_widget(Divider(height=2))
        layoutContent.add_widget(self._list_view)
        layoutContent.add_widget(Divider(height=1))
        layoutContent.add_widget(Text(label='Status:',name=self._model.out,readonly=True))
        layout = Layout([1,1,1,1])
        self.add_layout(layout)
        layout.add_widget(self._edit_button,0)
        layout.add_widget(Button('Users Info',self._informationUsers),1)
        layout.add_widget(Button('EXIT',self._exit),3)
        layout.add_widget(Button('EXIT TO MAIN',self._returnToMain),3)
        self.fix()
        self._on_pick()
        #print(model.getAllLocketAccounts())
        #layout.add_widget(self._list_view)
    def _informationUsers(self):
        raise NextScene('UsersDisplay')
    def _exit(self):
        raise StopApplication("User requested exit")
    def _on_pick(self):
        self._edit_button.disabled = self._list_view.value is None
        #self._reloadList()
    def _reloadList(self,*args):
        self.save()
        self._model.updateSettings()
        locket = self._model.getAllLocketAccounts()
        self._list_view.options = locket
    def _edit(self):
        self.save()
        arg = self.data['locketUsers']
        #self._model.configs = self._model.settings.get(arg['user']['name'])
        # obtenemos el ususario seleccionado
        # seteamos model con configs
        # XXX: SOLUCIONAR ESTO CREAR OTRO DICCIONARIO PARA ESTO 
        
        self._model.unlockAccount(name=arg['user']['name'])
        self._reloadList()
        #print(self._model.settings.get(arg['user']['name']))
        
        #self._model.userSelected = self._model.settings.get(arg['user']['name'])
        #print(self._model.userSelected)
        #raise NextScene('Info')
    def _returnToMain(self):
        raise NextScene('Main')      
class NewUser(Frame):
    def __init__(self, screen,model):
        super(NewUser,self).__init__(
            screen,
            height=screen.height * 2 // 3,
            width=screen.width * 2 // 3,
            hover_focus=True,
            title="newUser"
        )
        self._screen = screen
        self.set_theme('green')
        self._model = model
        #name:str,password:str,scrypt_level_security:int,save_path:str
        layout = Layout([100],fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Divider(height=4,draw_line=False),0)
        layout.add_widget(Text(label='name',name='name'),0)
        layout.add_widget(Text(label='password',name='password',hide_char=' '),0)
        layout.add_widget(Text(label='level security',name='scrypt_level_security',validator=r'\d'),0)
        exitLayout = Layout([1,1,1,1])
        self.add_layout(exitLayout)
        exitLayout.add_widget(Divider(draw_line=False,height=10))
        exitLayout.add_widget(Button(text='SUBMIT',on_click=self._submit),0)
        exitLayout.add_widget(Button(text='CANCEL',on_click=self._close),0)
        self.fix()
    def _submit(self):
        self.save()
        data = self.data
        # comporbamos si nombre no existe como usuario
        if not(data['name'] in self._model.getActiveUsers()):
            data['name'] = data['name'].lower()
            data['save_path'] = r'password.txt'
            # default path to save the passwords
            self._model.createNewUser(**data)
            self._model.updateSettings()
            #print(self._model.settings)
            raise NextScene('Main')
        self._scene.add_effect(PopUpDialog(self._screen,text="USER ALREADY REGISTRED!",buttons=['OK']))
        #raise NextScene('Main')
    
    def _close(self):
        raise NextScene('Main')
    def reset(self):
        # Do standard reset to clear out form, then populate with new data.
        super(NewUser, self).reset()
class MainView(Frame):
    def __init__(self, screen,model):
        super(MainView,self).__init__(screen,
        #height=screen.height,
        #width=screen.width * 2 // 2,
        height=screen.height * 2 // 3,
        width=screen.width * 2 // 3,
        hover_focus=True,
        title="Psec")
        self.set_theme(theme="green")
        self._out = ""
        self._model = model
        end_layout = Layout([30,70])
        self.add_layout(end_layout)
        end_layout.add_widget(Text("Status:",'status',readonly=True),1)
        layout = Layout([20,80],fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Divider(height=3,draw_line=False),1)
        layout.add_widget(Text("User:","user"),1)
        layout.add_widget(Text("Password:","password",hide_char="*"),1)
        layout.add_widget(Divider(height=13,draw_line=False),1)
        layout_buttom = Layout([1,1,1])
        self.add_layout(layout_buttom)
        layout_buttom.add_widget(Button("OK",self._ok),0)
        layout_buttom.add_widget(Button("CREATE NEW USER",self._newUser),2)
        #layout_buttom.add_widget(Button("CANCEL",self._cancel),2)
        self.fix()
    def reset(self):
        # Do standard reset to clear out form, then populate with new data.
        super(MainView, self).reset()
    @staticmethod
    def _cancel():
        pass
        #raise StopApplication("User requested exit")
        #raise NextScene("Main")
    def _showMessage(self,messaje):
        self.save()
        cp = self.data
        cp['status'] = messaje
        self.data = cp
    def _newUser(self):
        #self._showMessage('Funcion aun no disponible! ... ')
        raise NextScene('newUser')
    def _ok(self):
        #if self._model.isLocked:
        #    raise StopApplication("User requested exit")
        self.save()
        self._model.user = self.data['user']
        self._model.password = self.data['password']
        rsp = self._model.logn()
        self._showMessage(messaje=self._model.out)
        if self._model.isAdmin and rsp:
            #print(self._model.isAdmin)
            raise NextScene('AdminDisplay')
        if rsp:
            raise StopApplication("User requested exit")
        #raise StopApplication("User requested exit")
        # guardamos los datos en el cache introducido ahora validaremos
def demo(screen:Screen, scene):
    scenes = [
        #Scene([
        #    RandomNoise(screen,signal=FigletText("BLWSL",font='poison'))
        #],300,name='Banner'),
        Scene([
            Julia(screen),
            MainView(screen,model)], -1, name="Main"),
        Scene([NewUser(screen, model)],-1,name='newUser'),
        Scene([basic(screen, model),AdminDisplay(screen,model)],-1,name='AdminDisplay'),
        Scene([Print(screen,
                  ColourImageFile(screen, 
                                  r'D:\scripts\python\BLWSL\settings\death2.jpg',
                                  height=screen.height,
                                  uni=True,
                                  dither=True,
                                  fill_background=True
                                  ),
                  y=0,
                  x=int(screen.width * 0.01),
                  stop_frame=0 
                  ),UsersDisplay(screen, model)],-1,name='UsersDisplay'),#UsersDisplay(screen, model),
        Scene([AcountInfo(screen,model)],-1,name='Info')
    ]
    #screen._frame 
    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)#unhandled_input=shortcuts)
last_scene = None
model = Model(out='')
## si se resizea el screen
## entonces almacenaremos en esta vareable
## el screen actual para volver a mostrarlo
#
while True:
    try:
        Screen.wrapper(demo,catch_interrupt=True, arguments=[last_scene])
        exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
#BUG: AL CREAR UN NUEVO USUARIO DEBE SER NECESARIO RECARGAR EL PROGRAMA PARA QUE 
# NO TIRE EL ERROR USUARIO DESCONOCIDO ...