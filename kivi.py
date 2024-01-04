from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList,OneLineListItem
from kivy.lang.builder import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.navigationdrawer import MDNavigationDrawer,MDNavigationDrawerMenu
from kivymd.uix.card import MDCard
from kivymd.uix.backdrop import MDBackdrop
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton,MDRaisedButton,MDRoundFlatButton,MDFillRoundFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView


#style = """
#
#MDBoxLayout:
#   
#   orientation:"vertical"
#   padding:100
#   spacing:20
#
#   MDTextField:
#      
#      hint_text:"Enter your Email"
#      helper_tetx:"Username must be unique"
#      helper_text_mode:"on_focus"
#      icon_left:"account"
#      pos_hint:{"center_x": 0.5, "center_y": 0.5}
#      size_hint_x:None
#      width:300
#
#   MDTextField:
#      
#      hint_text:"Enter your Password"
#      helper_tetx:"Use strong password"
#      helper_text_mode:"on_focus"
#      icon_left:"lock-off"
#      pos_hint:{"center_x": 0.5, "center_y": 0.5}
#      size_hint_x:None
#      width:300
#
#   MDRaisedButton:
#      
#      text:"Login"
#      pos_hint:{"center_x": 0.5, "center_y": 0.5}
#
#
#
#
#"""


list = """
MDScrollView:
   MDList:
      OneLineListItem:
         
         text:"Item-1"
         IconLeftWidget:
            icon:"github"
        

"""


class txt(MDApp):
    def build(self):
        scrn = MDScreen()
        bldr = Builder.load_string(style)
        scrn.add_widget(bldr)
        return scrn

class txt2(MDApp):
    def build(self):
        view = MDScrollView()
        mylist = MDList()
        l1 = OneLineListItem(text="Item1")
        for i in range(1,20):
            v = OneLineListItem(text=f"Item{i}")
            mylist.add_widget(v)
        #mylist.add_widget(l1)
        view.add_widget(mylist)
        return view
    
class txt3(MDApp):
    def build(self):
        bldr = Builder.load_string(list)
        scrn = MDScreen()
        scrn.add_widget(bldr)
        return scrn

        

if __name__ == '__main__':
    txt3().run()