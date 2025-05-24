'''
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.username_input = TextInput(hint_text="Username")
        layout.add_widget(self.username_input)

        self.password_input = TextInput(hint_text="Password", password=True)
        layout.add_widget(self.password_input)

        login_button = Button(text="Login")
        login_button.bind(on_press=self.on_login)  # Bind the login button to a function
        layout.add_widget(login_button)

        self.add_widget(layout)

    def on_login(self, instance):
        # Here you can validate username and password or navigate to the dashboard
        # For now, let's just switch to the dashboard screen
        self.manager.current = "dashboard"  # Switch to the dashboard screen

'''
'''
kwargs is used to pass the numbers of different types of variables to the function

'''

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from db_handler import get_user, verify_password
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


Builder.load_file("screens/logic_screen.kv")
# The above line loads the kv file for the login screen

class LoginScreen(Screen):
    def login(self):
        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()
        stored_hash = get_user(username)
        if stored_hash and verify_password(stored_hash, password):
            self.manager.current = "dashboard"
        else:
            self.show_popup("Error", "Invalid username or password.")
    

    def go_to_register(self):
        self.manager.current = "register"

    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(Label(text=message))

        close_button = Button(text="Close", size_hint=(1, 0.3))
        layout.add_widget(close_button)

        popup = Popup(title=title, content=layout,
                      size_hint=(None, None), size=(300, 200), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()


