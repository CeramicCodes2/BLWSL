from Model import Model
from asciimatics.widgets import Frame,Button,Text,Layout,Divider
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics.effects import RandomNoise
from asciimatics.renderers import FigletText

class NewUser(Frame):
    def __init__(self, screen,model):
        super(NewUser,self).__init__(
            screen,
            height=screen.height * 2 // 3,
            width=screen.width * 2 // 3,
            hover_focus=True,
            title="newUser"
        )
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
        exitLayout.add_widget(Button(text='CANCEL',on_click=self._close))
        self.fix()
    def _submit(self):
        self.save()
        data = self.data
        data['name'] = data['name'].lower()
        data['save_path'] = r'D:\scripts\python\BLWSL\password.txt'
        # default path to save the passwords
        self._model.createNewUser(**data)
        raise NextScene('Main')
    @classmethod
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
        layout_buttom.add_widget(Button("CREATE NEW USER",self._newUser),1)
        layout_buttom.add_widget(Button("CANCEL",self._cancel),2)
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
        self._model.logn()
        #print(self.data)
        
        self._showMessage(messaje=self._model.out)
        # guardamos los datos en el cache introducido ahora validaremos

def demo(screen, scene):
    scenes = [
        #Scene([
        #    RandomNoise(screen,signal=FigletText("BLWSL",font='poison'))
        #],300,name='Banner'),
        Scene([MainView(screen,model)], -1, name="Main"),
        Scene([NewUser(screen, model)],-1,name='newUser')
    ]
    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)
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