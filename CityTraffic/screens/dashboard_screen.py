from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        check_traffic_button = Button(text="Check Traffic")
        check_traffic_button.bind(on_press=self.on_check_traffic)
        layout.add_widget(check_traffic_button)

        self.add_widget(layout)

    def on_check_traffic(self, instance):
        # For now, just print something (you can replace this with actual traffic checking logic)
        print("Checking traffic status...")  # Later add your code to display traffic and alternative routes
