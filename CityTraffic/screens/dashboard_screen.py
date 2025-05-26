from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.metrics import dp # Import dp for consistent sizing

# Load the corresponding .kv file for this screen
Builder.load_file('screens/dashboard_screen.kv')

class DashboardScreen(Screen): # subclass of screen later used as a custom screen class in kv file
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # The layout is handled by the .kv file, so no need to add widgets here.

    def on_check_traffic(self):
        # This method seems to be for a specific action within the dashboard,
        # not directly related to screen navigation buttons in the sidebar.
        # It's good practice to keep it if it's used elsewhere.
        origin = self.ids.origin_input.text if 'origin_input' in self.ids else "N/A"
        destination = self.ids.destination_input.text if 'destination_input' in self.ids else "N/A"
        
        # Replace with your actual logic for checking traffic
        # If content_label exists, update it.
        if 'content_label' in self.ids:
            self.ids.content_label.text = "Checking traffic status..."
        print(f"Checking traffic status from {origin} to {destination}...") # Simulate checking traffic

    def logout(self):
        """
        Logs out the user from the dashboard and navigates back to the login screen.
        """
        print("User logged out from Dashboard.")
        # You might want to clear any session data here if you have it
        # For example: App.get_running_app().user_data = None
        self.manager.current = "login" # Navigate back to the login screen
        # Optional: Add a transition effect
        # self.manager.transition.direction = 'right'

