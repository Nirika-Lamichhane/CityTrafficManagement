from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

# Load the corresponding .kv file for this screen
Builder.load_file('screens/dashboard_screen.kv')

class DashboardScreen(Screen): #subclass of screen later used as a custom screen class in kv file
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # The layout is handled by the .kv file, so no need to add widgets here.

    def on_check_traffic(self):
        # Replace with your actual logic for checking traffic
        self.ids.content_label.text = "Checking traffic status..."
        print("Checking traffic status...")  # Simulate checking traffic

    def on_shortest_path(self):
        # Replace with your logic to show the shortest path
        self.ids.content_label.text = "Showing shortest path..."
        print("Showing shortest path...")  # Simulate shortest path calculation
