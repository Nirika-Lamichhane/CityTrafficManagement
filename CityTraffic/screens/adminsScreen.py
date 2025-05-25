import csv
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle # Import for drawing backgrounds

# Load the KV file. Ensure this path matches where your KV file is saved.
# If your KV file is named 'admindashboard.kv' and is in the same directory, use that.
# If it's in 'screens/adminsScreen.kv' as per your original code, ensure that path is correct.
# For consistency with the provided KV immersive, let's assume it's named 'admindashboard.kv'
# and is in the same directory as this Python file for simplicity.
Builder.load_file("screens/adminsScreen.kv")


class AdminDashboard(Screen):
    # ListProperty to hold user data, allowing Kivy to observe changes
    users = ListProperty([])

    def on_enter(self):
        """
        Called when the screen becomes active.
        Responsible for loading initial user data and populating the table.
        """
        # Schedule the initial loading of users after the UI has been built
        # This prevents issues with accessing self.ids before the KV is fully processed
        Clock.schedule_once(self._load_users_initial, 0)

    def _load_users_initial(self, dt):
        """
        Loads initial dummy user data.
        In a real application, this would fetch data from a database or API.
        """
        # Dummy user data - replace with real DB queries
        # This data structure aligns with the columns in your KV file:
        # Username, Name, Email, Last Login, Status
        self.users = [
            {"username": "johndoe", "name": "John Doe", "email": "john@example.com", "last_login": "10:05 AM", "status": "Active"},
            {"username": "janedoe", "name": "Jane Doe", "email": "jane@example.com", "last_login": "09:45 AM", "status": "Inactive"},
            {"username": "admin_user", "name": "Admin User", "email": "admin@example.com", "last_login": "08:30 AM", "status": "Active"},
            {"username": "testuser1", "name": "Test User One", "email": "test1@example.com", "last_login": "11:00 AM", "status": "Active"},
            {"username": "anotheruser", "name": "Another User", "email": "another@example.com", "last_login": "07:15 AM", "status": "Inactive"},
            {"username": "kivydev", "name": "Kivy Developer", "email": "dev@kivy.org", "last_login": "01:20 PM", "status": "Active"},
            {"username": "guest_account", "name": "Guest Account", "email": "guest@example.com", "last_login": "02:00 PM", "status": "Active"},
            {"username": "blocked_user", "name": "Blocked User", "email": "blocked@example.com", "last_login": "03:40 PM", "status": "Suspended"},
            {"username": "new_signup", "name": "New Signup", "email": "new@example.com", "last_login": "04:55 PM", "status": "Pending"},
        ]
        self.populate_table()

        # For real-time updates, you would typically set up a database listener here.
        # Example (conceptual, for a database like Firebase Firestore):
        # self.db_listener = db.collection('users').on_snapshot(self._on_users_db_update)

    # def _on_users_db_update(self, col_snapshot, changes, read_time):
    #     """
    #     Conceptual callback for real-time database updates.
    #     This method would be triggered by your database client when data changes.
    #     """
    #     print("Database update received, refreshing user table.")
    #     # In a real scenario, you'd parse `changes` to incrementally update `self.users`
    #     # For simplicity, we'll re-fetch or re-assign `self.users` and then re-populate.
    #     # self.users = [user_data_from_snapshot_or_changes]
    #     # self.populate_table()


    def populate_table(self):
        """
        Populates the user table (GridLayout) with headers and user data.
        Ensures the table is scrollable by setting height based on minimum_height.
        """
        table_layout = self.ids.user_table
        table_layout.clear_widgets() # Clear existing entries before repopulating

        # Define headers for the table
        headers = ["Username", "Name", "Email", "Last Login", "Status"]

        # Add header labels with specific styling
        for header_text in headers:
            header_label = Label(
                text=header_text,
                bold=True,
                color=(0, 0, 0, 1), # Black text for headers
                size_hint_y=None,
                height=dp(40) # Ensure header height matches row_default_height
            )
            # Add a light grey background to the header cells
            with header_label.canvas.before:
                Color(0.85, 0.85, 0.85, 1) # Light grey background
                Rectangle(pos=header_label.pos, size=header_label.size)
            table_layout.add_widget(header_label)

        # Add user data rows
        for user in self.users:
            # Use the make_label helper, ensuring text color is black
            table_layout.add_widget(self.make_label(user.get("username", "")))
            table_layout.add_widget(self.make_label(user.get("name", "")))
            table_layout.add_widget(self.make_label(user.get("email", "")))
            table_layout.add_widget(self.make_label(user.get("last_login", "")))
            table_layout.add_widget(self.make_label(user.get("status", "")))

        # Crucial for ScrollView: Update the GridLayout's height to its minimum required height
        # This makes the ScrollView functional when content exceeds visible area.
        table_layout.height = table_layout.minimum_height

    def make_label(self, text):
        """
        Helper function to create a Label with consistent styling for table cells.
        """
        return Label(
            text=text,
            size_hint_y=None,
            height=dp(40), # Match row_default_height from KV
            color=(0, 0, 0, 1) # Black text for data cells
        )

    def logout(self):
        """
        Handles the logout action.
        Navigates back to the login screen.
        """
        self.show_message("Logout", "Logging out...")
        # Assuming 'login' is the name of your login screen in the ScreenManager
        if self.manager:
            self.manager.current = "login"
        else:
            print("Error: ScreenManager not found for logout.")


    def export_users(self):
        """
        Exports the current user data to a CSV file.
        """
        if not self.users:
            self.show_message("Export Failed", "No user data available to export.")
            return

        # Define the file path for the CSV.
        # In a production app, you might want to use a FileChooserPopup
        # to let the user select the save location.
        file_path = "exported_user_data.csv"

        try:
            # Determine fieldnames from the first user dictionary's keys
            # or explicitly define them if you have a fixed schema.
            # Using a fixed schema is safer for CSV export.
            fieldnames = ["username", "name", "email", "last_login", "status"]

            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader() # Write the header row
                for user in self.users:
                    # Write each user dictionary as a row
                    writer.writerow(user)

            self.show_message("Export Successful", f"User data exported to:\n{file_path}")
            print(f"User data exported to {file_path}")

        except IOError as e:
            self.show_message("Export Error", f"Could not write to file:\n{e}")
            print(f"Error writing CSV file: {e}")
        except Exception as e:
            self.show_message("Export Error", f"An unexpected error occurred:\n{e}")
            print(f"An unexpected error occurred during export: {e}")

    def show_message(self, title, message):
        """
        Displays a custom message popup to the user.
        Replaces alert() or print() for user feedback.
        Updated: Text color is white, background color is black.
        """
        content = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        # Set the background color of the content BoxLayout to black
        with content.canvas.before:
            Color(0, 0, 0, 1)  # Black background
            Rectangle(pos=content.pos, size=content.size)

        content.add_widget(Label(text=message, color=(1,1,1,1), halign='center', valign='middle')) # White text
        close_button = Button(text="OK", size_hint_y=None, height=dp(40))
        content.add_widget(close_button)

        popup = Popup(title=title, content=content, size_hint=(0.7, 0.4),
                      auto_dismiss=False)
        # Set the popup's background color if needed (title bar is separate)
        # For a completely black popup, you might also need to style the title bar
        # For now, the content area will be black.
        close_button.bind(on_release=popup.dismiss)
        popup.open()


# Example of how to run this screen in a full Kivy App
# (This part would typically be in your main.py or app.py)
if __name__ == '__main__':
    from kivy.app import App
    from kivy.uix.screenmanager import ScreenManager

    class TestApp(App):
        def build(self):
            sm = ScreenManager()
            # It's important that the name 'login' matches what your logout function expects
            # and that 'admin_dashboard' matches the name used to navigate to this screen.
            sm.add_widget(Screen(name='login')) # Dummy login screen
            sm.add_widget(AdminDashboard(name='admin_dashboard'))
            sm.current = 'admin_dashboard' # Start on the admin dashboard for testing
            return sm

    TestApp().run()
