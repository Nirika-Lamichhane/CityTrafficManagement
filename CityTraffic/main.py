from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import ScreenManager

from screens.login_screen import LoginScreen
from screens.dashboard_screen import DashboardScreen
from screens.checktraffic import CheckTrafficScreen
from screens.shortest import ShortestPathScreen
from screens.register_Screen import RegisterScreen
from screens.adminsScreen import AdminDashboard

from db_handler import create_table, add_login_time_column


class CityTrafficApp(App):
    logged_in_users = []
    notifications_enabled = BooleanProperty(False)

    def add_user_login(self, username, name, email):
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        self.logged_in_users.append({
            "username": username,
            "name": name,
            "email": email,
            "last_login": now,
            "status": "Active"
        })

    def ask_notification_permission(self):
        # Toggle the state
        self.notifications_enabled = not self.notifications_enabled

        # Simulate sending request to backend if needed
        if self.notifications_enabled:
            print("Notifications enabled. (Simulate sending token to server)")
        else:
            print("Notifications disabled. (Simulate removing token from server)")

    def build(self):
        sm = ScreenManager()
        create_table()
        add_login_time_column()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(CheckTrafficScreen(name='check_traffic'))
        sm.add_widget(ShortestPathScreen(name='shortest_path'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(AdminDashboard(name='admin_dashboard'))
        print(f"Screens in screen manager: {sm.screens}")
        return sm


if __name__ == '__main__':
    CityTrafficApp().run()
