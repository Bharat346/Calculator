from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.chip import MDChip
from kivymd.uix.circularlayout import MDCircularLayout

KV = '''
BoxLayout:
    orientation: 'vertical'

    ScrollView:
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(10)

            MDChip:
                label: 'Work'
                icon: 'briefcase'
                on_release: app.chip_callback(self, 'Work')

            MDChip:
                label: 'Personal'
                icon: 'heart'
                on_release: app.chip_callback(self, 'Personal')

            MDChip:
                label: 'Shopping'
                icon: 'cart'
                on_release: app.chip_callback(self, 'Shopping')

            # ... Additional MDChip instances for more categories

'''

class TaskManagerApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def chip_callback(self, chip_instance, category):
        print(f"Tasks related to '{category}' category.")

if __name__ == '__main__':
    TaskManagerApp().run()
