from kivy.app import App
# imports app class from kivy.app module of kivy library

from kivy.uix.screenmanager import ScreenManager
from screens.login_screen import LoginScreen
from screens.dashboard_screen import DashboardScreen
from screens.checktraffic import CheckTrafficScreen

class CityTrafficApp(App): # class that inherits from app class 

    def build(self): # build is method of app class which is used to build the app
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(CheckTrafficScreen(name='check_traffic')) # add widget to the screen manager
        return sm
if __name__ == '__main__':
     CityTrafficApp().run()

'''
name is built in python variable
init is the special method used for initializing the classes like constructor

'''