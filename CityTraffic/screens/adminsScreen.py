import csv
import os
from datetime import datetime

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.clock import Clock

# Android storage path handling (optional on PC)
try:
    from android.storage import primary_external_storage_path
except:
    primary_external_storage_path = None

# Assuming db_handler.py is in the same directory
from db_handler import fetch_logged_in_users

# Load the KV file (adjust if path is different)
Builder.load_file("screens/adminsScreen.kv")

class AdminDashboard(Screen):
    """
    AdminDashboard screen for managing and viewing user data.
    """

    def on_enter(self, *args):
        """
        Called when the screen is entered. Schedules refreshing the user table.
        """
        Clock.schedule_once(self.refresh_users_table, 0)

    def refresh_users_table(self, dt):
        """
        Populates the user_table GridLayout with data.
        """
        user_table = self.ids.user_table
        user_table.clear_widgets()
        users_data = fetch_logged_in_users()

        col_widths_ratio = {
            'username': 0.2,
            'login_time': 0.3,
            'role': 0.2,
            'status': 0.3
        }

        grid_width = user_table.width - dp(10)
        if grid_width <= 0:
            grid_width = dp(400)

        for user in users_data:
            username_text = str(user.get('username', ''))
            login_time_text = str(user.get('login_time', 'N/A'))
            role_text = "User"    # Placeholder
            status_text = "Active" # Placeholder

            user_table.add_widget(Label(
                text=username_text,
                halign='center',
                valign='middle',
                text_size=(grid_width * col_widths_ratio['username'], None),
                color=(0, 0, 0, 1),
                size_hint_x=col_widths_ratio['username']
            ))

            user_table.add_widget(Label(
                text=login_time_text,
                halign='center',
                valign='middle',
                text_size=(grid_width * col_widths_ratio['login_time'], None),
                color=(0, 0, 0, 1),
                size_hint_x=col_widths_ratio['login_time']
            ))

            user_table.add_widget(Label(
                text=role_text,
                halign='center',
                valign='middle',
                text_size=(grid_width * col_widths_ratio['role'], None),
                color=(0, 0, 0, 1),
                size_hint_x=col_widths_ratio['role']
            ))

            user_table.add_widget(Label(
                text=status_text,
                halign='center',
                valign='middle',
                text_size=(grid_width * col_widths_ratio['status'], None),
                color=(0, 0, 0, 1),
                size_hint_x=col_widths_ratio['status']
            ))

    def export_users(self):
        """
        Exports user data to a CSV file in Downloads folder on Android.
        """
        try:
            users_data = fetch_logged_in_users()
            fieldnames = ['username', 'login_time']
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"exported_users_{timestamp}.csv"

            # Determine export path (Android or fallback)
            if primary_external_storage_path:
                downloads_dir = os.path.join(primary_external_storage_path(), "Download")
            else:
                downloads_dir = os.path.join(os.getcwd(), "exports")

            if not os.path.exists(downloads_dir):
                os.makedirs(downloads_dir)

            filepath = os.path.join(downloads_dir, filename)

            with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(users_data)

            self.show_popup("Success", f"File exported to:\n{filepath}")

        except Exception as e:
            self.show_popup("Export Error", f"An error occurred:\n{e}")
            import traceback
            traceback.print_exc()

    def logout(self):
        """
        Logs out the admin and navigates back to login screen.
        """
        self.manager.current = "login"

    def show_popup(self, title, message):
        """
        Displays a popup with custom message.
        """
        layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))

        msg_label = Label(
            text=message,
            halign='center',
            valign='middle',
            size_hint_y=None,
            height=dp(80)
        )
        msg_label.bind(width=lambda instance, value:
                       setattr(instance, 'text_size', (value, None)))

        layout.add_widget(msg_label)

        close_button = Button(text="OK", size_hint=(1, 0.3))
        layout.add_widget(close_button)

        popup = Popup(title=title, content=layout,
                      size_hint=(None, None), size=(dp(300), dp(200)), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()
