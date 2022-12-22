from Model import Model
from asciimatics.widgets import Frame,Button,Text,Layout,Divider
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics.effects import RandomNoise
from asciimatics.renderers import FigletText
class MainView(Frame):
    def __init__(self, screen):
        super(MainView,self).__init__(screen,
        #height=screen.height,
        #width=screen.width * 2 // 2,
        height=screen.height * 2 // 3,
        width=screen.width * 2 // 3,
        hover_focus=True,
        title="Psec")
        self.set_theme(theme="green")
        self._out = ""
        self._model = Model(out=self._out)
        end_layout = Layout([30,70])
        self.add_layout(end_layout)
        end_layout.add_widget(Text("Status:",self._out,readonly=True),1)
        layout = Layout([20,80])
        self.add_layout(layout)
        layout.add_widget(Divider(height=3,draw_line=False),1)
        layout.add_widget(Text("User:","user"),1)
        layout.add_widget(Text("Password:","password",hide_char="*"),1)
        layout.add_widget(Divider(height=13,draw_line=False),1)
        layout_buttom = Layout([1,1,1])
        self.add_layout(layout_buttom)
        layout_buttom.add_widget(Button("OK",self._ok),0)
        layout_buttom.add_widget(Button("CANCEL",self._cancel),2)
        self.fix()
    def reset(self):
        # Do standard reset to clear out form, then populate with new data.
        super(MainView, self).reset()
    @staticmethod
    def _cancel():
        raise StopApplication("User requested exit")
        #raise NextScene("Main")
    def _ok(self):
        if self._model.isLocked:
            raise StopApplication("User requested exit")
        self.save()
        self._model.user = self.data['user']
        self._model.password = self.data['password']
        self._model.logn()
        # guardamos los datos en el cache introducido ahora validaremos
def demo(screen, scene):
    scenes = [
        #Scene([
        #    RandomNoise(screen,signal=FigletText("Psec",font='poison'))
        #],300,name='Banner'),
        Scene([MainView(screen)], -1, name="Main"),
    ]
    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)
last_scene = None
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