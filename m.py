from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class Home(Screen):
    pass

class First_screen(Screen):
    pass

class manager(ScreenManager):
    pass

class btn(App):
    def build(self):
        # Set the background color to white
        Window.clearcolor = (1, 1, 1, 1)
        lay = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        img = Image(source="me.jpg", size_hint=(None, None), width=200, height=100, pos_hint={"center_x": 0.5, "center_y": 0.5})
        lab = Label(text="Hello Guys...", font_size="120sp", bold=True, italic=True, color=(1, 0, 0, 1))
        btn1 = Button(text="Click me-1", size_hint=(0.3, 0.4), pos_hint={"center_x": 0.5, "center_y": 0.5}, on_release=self.btn_click)
        btn2 = Button(text="Click me-2", size_hint=(0.3, 0.4), pos_hint={"center_x": 0.5, "center_y": 0.5}, on_release=self.btn_click)
        btn3 = Button(text="Click me-3", size_hint=(0.3, 0.4), pos_hint={"center_x": 0.5, "center_y": 0.5}, on_release=self.btn_click)
        btn4 = Button(text="Click me-4", size_hint=(0.3, 0.4), pos_hint={"center_x": 0.5, "center_y": 0.5}, on_release=self.btn_click)
        lay.add_widget(btn1)
        lay.add_widget(btn2)
        lay.add_widget(btn3)
        lay.add_widget(btn4)
        return lay
    
    def btn_click(self, instance):
        print("Button clicked")

class my_app(App):
    def build(self):
        lay1 = BoxLayout(orientation="vertical", spacing=10, padding=250)
        self.email = TextInput(text="Enter your Email")
        self.password = TextInput(text="Enter your Password")
        self.submit_button = Button(text="Login", on_press=self.submit_btn)
        lay1.add_widget(self.email)
        lay1.add_widget(self.password)
        lay1.add_widget(self.submit_button)
        return lay1
    
    def submit_btn(self, instance):
        print(f"Email : {self.email.text}")
        print(f"Password : {self.password.text}")

class anc(App):
    def build(self):
        layout = AnchorLayout(anchor_x='right',anchor_y='bottom')
        btn1 = Button(text="Bharat",size_hint=(None,None),width=100)
        layout.add_widget(btn1)
        return layout
        
class hello(App):
    def build(self):
        pass 
    
if __name__ == '__main__':
    hello().run()
