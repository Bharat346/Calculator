from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDSpinner:
        id: spinner
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': 0.5}
        active: False  # Set to True to start the spinner

    MDRaisedButton:
        text: "Toggle Spinner"
        pos_hint: {'center_x': 0.5}
        on_release: app.toggle_spinner()
'''

class SpinnerApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def toggle_spinner(self):
        spinner = self.root.ids.spinner
        spinner.active = not spinner.active

if __name__ == '__main__':
    SpinnerApp().run()
