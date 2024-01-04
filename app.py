from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.label import MDIcon
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton,MDRaisedButton,MDRoundFlatButton,MDFillRoundFlatButton

from kivy.uix.boxlayout import BoxLayout

class Hello(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.primary_hue = "600"
        btn = MDFlatButton(text="Click me",pos_hint={"center_x":0.5,"center_y":0.5})
        btn2 = MDRectangleFlatButton(text="rect_btn",pos_hint={"center_x":0.5,"center_y":0.5})
        btn3 = MDIconButton(icon="android",pos_hint={"center_x":0.5,"center_y":0.5})
        btn4 = MDFloatingActionButton(icon="android",pos_hint={"center_x":0.5,"center_y":0.5})
        btn5 = MDRaisedButton(text="raise_btn",pos_hint={"center_x":0.5,"center_y":0.5})
        btn6 = MDRoundFlatButton(text="raise_btn",pos_hint={"center_x":0.5,"center_y":0.5})
        btn7 = MDFillRoundFlatButton(text="raise_btn",pos_hint={"center_x":0.5,"center_y":0.5})
        btn8 = MDRaisedButton(text="Dark-Theme",pos_hint={"center_x":0.5,"center_y":0.5})
        
        #icon = MDIcon(icon="menu-down",pos_hint={"center_x":0.5,"center_y":0.5}, font_size="48sp")  # Use a valid icon name from :https://pictogrammers.com/library/mdi/

        return btn8

if __name__ == '__main__':
    Hello().run()
