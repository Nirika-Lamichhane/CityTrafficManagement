from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from db_handler import get_user, verify_password, update_last_login
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from datetime import datetime


Builder.load_file("screens/logic_screen.kv")  # Loads the login KV file

class LoginScreen(Screen):

    def login(self):
        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()

        if username == "admin":
            admin_password = "admin123"
            if password == admin_password:
                self.manager.current = "admin_dashboard"
                return
            else:
                self.show_popup("Error", "Invalid admin password.")
                return

        stored_hash = get_user(username)
        if stored_hash and verify_password(stored_hash, password):
            # ✅ Update last login time
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            update_last_login(username, now_str)

       

            # ✅ Navigate to dashboard
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
