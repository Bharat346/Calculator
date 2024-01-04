from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.chip import MDChip
from kivymd.uix.navigationdrawer import MDNavigationDrawer,MDNavigationDrawerMenu
from kivymd.uix.card import MDCard
from kivymd.uix.backdrop import MDBackdrop
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton,MDRaisedButton,MDRoundFlatButton,MDFillRoundFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

class MyApp(MDApp):
    def build(self):
        # Create a BoxLayout to hold the cards
        layout = MDBoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create two cards
        card1 = MDCard(
            orientation='vertical',
            padding=10,
            size_hint=(None, None),
            size=(300, 200),
            md_bg_color=(0.8, 0.2, 0.2, 1)
        )
        card1.add_widget(MDLabel(text='Card 1 Content'))

        card2 = MDCard(
            orientation='vertical',
            padding=10,
            size_hint=(None, None),
            size=(300, 200),
            md_bg_color=(0.2, 0.7, 0.2, 1)
        )
        card2.add_widget(MDLabel(text='Card 2 Content'))

        # Add cards to the layout
        layout.add_widget(card1)
        layout.add_widget(card2)

        return layout


class draw(MDApp):
    def build(self):
        # Create the main container
        layout = MDBoxLayout(orientation='vertical')

        # Create a button to open the navigation drawer
        nav_button = MDRaisedButton(text='Open Drawer', on_press=self.open_drawer)
        layout.add_widget(nav_button)

        return layout

    def open_drawer(self, instance):
        # Create an instance of MDNavigationDrawer
        nav_drawer = MDNavigationDrawer()

        # Create an instance of MDNavigationDrawerMenu
        nav_menu = MDNavigationDrawerMenu()

        # Add menu items
        nav_menu.items = [
            {"text": "Item 1", "viewclass": "OneLineListItem", "on_release": self.item_click},
            {"text": "Item 2", "viewclass": "OneLineListItem", "on_release": self.item_click},
            {"text": "Item 3", "viewclass": "OneLineListItem", "on_release": self.item_click},
        ]

        # Add the menu to the navigation drawer
        nav_drawer.add_widget(nav_menu)

        # Open the navigation drawer
        nav_drawer.toggle_nav_drawer()

    def item_click(self, instance):
        print(f"Clicked on {instance.text}")

if __name__ == "__main__":
    draw().run()
    
