from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.circularlayout import MDCircularLayout
from kivymd.uix.expansionpanel import MDExpansionPanel

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDCircularLayout:
        size_hint: None, None
        size: dp(200), dp(200)
        pos_hint: {'center_x': 0.5}
        
        MDRaisedButton:
            text: 'Button 1'
            on_release: app.button_callback(1)

        MDRaisedButton:
            text: 'Button 2'
            on_release: app.button_callback(2)

        MDRaisedButton:
            text: 'Button 3'
            on_release: app.button_callback(3)

        MDRaisedButton:
            text: 'Button 4'
            on_release: app.button_callback(4)
'''

class CircularLayoutApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def button_callback(self, button_number):
        print(f"Button {button_number} pressed")

if __name__ == '__main__':
    CircularLayoutApp().run()
