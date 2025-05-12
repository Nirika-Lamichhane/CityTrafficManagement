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

Builder.load_file("screens/logic_screen.kv")
# The above line loads the kv file for the login screen

class LoginScreen(Screen):
    def login(self):
        username = self.ids.username.text
        password = self.ids.password.text
        if username == "admins" and password == "123":
            print("Login successful!")
            self.manager.current = "dashboard" #switch to the dashbard screen
        else:
            print("Invalid credentials")
