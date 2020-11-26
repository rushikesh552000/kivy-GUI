from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from database import DataBase 

Window.size=(350,500)


class MainWindow(Screen):
    user = ObjectProperty(None)
    password = ObjectProperty(None)


    def login(self):
        if db.validate(self.email.text, self.password.text):
            AWindow.current = self.email.text
          
            self.refresh()
            sm.current = "secondmain"
        else:
            self.error_btn()
                
    

        #"secondwindow" if password.text == "5508" and user.text == 'rushi' else root.error_btn()

    def error_btn(self):
        login_error()
    
    def refresh(self):
        self.email.text = ""
        self.password.text = ""



class AWindow(Screen):
    current = ""
    namee = ObjectProperty(None)
    contact = ObjectProperty(None)
    email = ObjectProperty(None)
    usernamee = ObjectProperty(None)
    password = ObjectProperty(None)
    created = ObjectProperty(None)
    
    
    
    
    def on_enter(self, *args):
        password, name,contact ,username,created = db.get_user(self.current)
        self.namee.text = "Name : " + name
        self.usernamee.text = "User Name : "+username
        self.contact.text = "Contact Number : "+contact
        self.email.text = "Email : " + self.current
        self.password.text = "Password : "+ password
        self.created.text = "Created On : " + created
 


class SignupWindow(Screen):

    namee =ObjectProperty(None)
    contact = ObjectProperty(None)
    email = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".")>0:
            if self.password!= "" and self.username != "": 
                db.add_user(self.email.text, self.password.text, self.namee.text,self.contact.text,self.username.text)
                self.reset()
                sm.current = "main"
            else:
                invalidform()
        else:
            invalidform()


    def reset(self):
    
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""
        self.contact.text = ""
        self.username.text = ""

class SecondMainWindow(Screen):
    pass
 


class PManager(ScreenManager):
    pass


class Loginerror(FloatLayout):
    pass
class Invalidform(FloatLayout):
    pass


def invalidform():
    show =Invalidform()
    pop = Popup(title='Invalid Form',
                  content=show,
                  size_hint=(None,None), size=(250, 200))

    pop.open()



def login_error():
    show = Loginerror()
    
    pop =Popup(title="login error", content=show,size_hint=(None,None),size =(250,200))

    pop.open()





kv = Builder.load_file('playmain.kv')
sm = PManager()

db = DataBase("users.txt")


screens = [MainWindow(name="main"),AWindow(name="awindow"),SignupWindow(name="signup"),SecondMainWindow(name="secondmain")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"




class InfoclgApp(App):
    def build(self):
        return sm
        
    def on_close(self, *args):
        App.get_running_app().stop()
    
if __name__ == "__main__":
    InfoclgApp().run()
