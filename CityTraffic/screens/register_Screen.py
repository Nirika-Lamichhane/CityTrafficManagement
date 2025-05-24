from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from auth import hash_password
from db_handler import insert_user

Builder.load_file("screens/register_Screen.kv")

class RegisterScreen(Screen):
    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None), size=(300, 200))
        popup.open()

    def register_user(self):
        username = self.ids.reg_username.text.strip()
        password = self.ids.reg_password.text.strip()

        if username == "" or password == "":
            self.show_popup("Error", "Username and password cannot be empty.")
            return

        hashed = hash_password(password)

        if insert_user(username, hashed):
            self.show_popup("Success", "Registration Completed!")
            self.manager.current = 'login'
        else:
            self.show_popup("Error", "Username already exists.")
