from kivy.app import App
from kivy.core import text
from kivy.uix.widget import Widget
#from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.metrics import dp 
from kivy.uix.gridlayout import GridLayout
from utils import Main
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.factory import Factory
from unipath import Path
from datetime import datetime
from kivy.lang import Builder

my_label = ''
#Builder.load_file('MainApp222.kv')
Window.clearcolor = (150/255,150/255,150/255,1)

class MainWG(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #Window.clearcolor = (150/255,150/255,150/255,1)
    def sttwav(self, filename):
        self.ids.label_update.text = 'Processing the file.....\nPlease wait....'
        print('Add started' + filename[0])        
        global my_label
        finalOutput = Main.seperation(filename[0], 'audio/wav')

        v = []
        for z in finalOutput:
            if 'newline' not in z.keys() :
                v.append(z['speaker']) #if 
        num_speakers = set(v)
         
        #my_label = ''
        for i in num_speakers:
            z = i
            s = ''
            for x in finalOutput:
                if 'newline' in x.keys():
                    s += '\n'
                elif x['speaker'] == z:
                    s += x['transcript'] + ' '
        
            #print('Speaker '+ str(i) + '\n' + s)
            
            my_label += '\nSpeaker '+ str(i) + '\n' + s 
               
        #pop()
        p = Path(filename[0])
        np = str(p.parent)
        print(my_label)
        dt = datetime.now()
        d = dt.strftime(("%Y-%m-%d %H-%M"))    
        with open(np + '\output' + d+'.txt', 'w') as f:
            f.write(my_label)
            f.close
        self.ids.label_update.text = 'Transcript saved at '+ np + '\output'+d+'.txt\nRestart to transcribe another file'
        print('file created ')

    def sttmp3(self, filename):
        self.ids.label_update.text = 'Processing the file.....\nPlease wait....'
        print('Add started' + filename[0])
        global my_label
        finalOutput = Main.seperation(filename[0], 'audio/mp3')

        v = []
        for z in finalOutput:
            if 'newline' not in z.keys() :
                v.append(z['speaker']) #if 
        num_speakers = set(v)
         
        #my_label = ''
        for i in num_speakers:
            z = i
            s = ''
            for x in finalOutput:
                if 'newline' in x.keys():
                    s += '\n'
                elif x['speaker'] == z:
                    s += x['transcript'] + ' '
        
            #print('Speaker '+ str(i) + '\n' + s)
            
            my_label += '\nSpeaker '+ str(i) + '\n' + s 
         
        #my_label = 'Demo text'
        
        #pop()
        p = Path(filename[0])
        np = str(p.parent)
        print(my_label)
        dt = datetime.now()
        d = dt.strftime(("%Y-%m-%d %H-%M"))    
        #self.ids.update_label.text = 'Some error occured'
        with open(np + '\output' + d+'.txt', 'w') as f:
            f.write(my_label)
            f.close
        
        print('file created ')
        self.ids.label_update.text = 'Transcript saved at '+ np + '\output'+d+'.txt\nRestart to transcribe another file'
        print(my_label)    
        #self.ids.update_label.text = 'Some error occured'
        
#make a pop up class then call it using factory/norml
class Gridlayout(GridLayout):
    
    def selected(self, filename): 
        address = filename[0]
        print(address + '0')
    
class Scroll(ScrollView):
    pass       
class MyPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.update_label.text = my_label

def pop():
    Factory.MyPopup().open()
    #self.ids.my_popup.ids.scr.ids.update_label.text = my_label   
    #self.app.ids.update_label.text = my_label
    #print(my_label)    
    #self.ids.update_label.text = 'Some error occured'

class MainApp(App):
    pass
if __name__ == '__main__':
    
    MainApp().run()