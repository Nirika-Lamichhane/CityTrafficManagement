from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
Builder.load_file("screens/register_Screen.kv")

class RegisterScreen(Screen):
    def register_user(self):
        username = self.ids.reg_username.text
        password = self.ids.reg_password.text
        # Save to file or database — basic example below
        with open("users.txt", "a") as f:
            f.write(f"{username},{password}\n")
        print("User registered!")
        self.manager.current = 'login'
