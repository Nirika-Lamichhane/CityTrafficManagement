from kivy.app import App
# imports app class from kivy.app module of kivy library

from kivy.uix.screenmanager import ScreenManager
from screens.login_screen import LoginScreen
from screens.dashboard_screen import DashboardScreen
from screens.checktraffic import CheckTrafficScreen
from screens.shortest import ShortestPathScreen
from screens.register_Screen import RegisterScreen
from db_handler import create_table
from screens.adminsScreen import AdminDashboard


class CityTrafficApp(App): # class that inherits from app class 
    
    logged_in_users = []  # store user login details

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

    def build(self): # build is method of app class which is used to build the app
        sm = ScreenManager()
        create_table()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard')) # here the name is given so as we can do scren transition
        sm.add_widget(CheckTrafficScreen(name='check_traffic')) # add widget to the screen manager
        sm.add_widget(ShortestPathScreen(name='shortest_path'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(AdminDashboard(name='admin_dashboard'))


        
        print (f"Screens in screenmanager:{sm.screens}")
        return sm
if __name__ == '__main__':
    CityTrafficApp().run()

'''
name is built in python variable
init is the special method used for initializing the classes like constructor

'''