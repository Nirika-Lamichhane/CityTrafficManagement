# screens/shortest.py
# This file defines the Python class for the Shortest Path Calculator screen.
# Place this file inside your 'screens' folder.

from kivy.uix.screenmanager import Screen # Import Screen
from kivy.uix.boxlayout import BoxLayout # Still need BoxLayout for the internal layout
from kivy.properties import StringProperty
from kivy.lang import Builder
import os

# --- Import Dijkstra Algorithm and city_map from the parent directory ---
# The '..' indicates going up one directory level from 'screens'.
from city_map import city_map
from dijkstra import dijkstra

# Load the KV file for this screen
# Construct the path to the KV file dynamically.
current_dir = os.path.dirname(os.path.abspath(__file__))
kv_file_path = os.path.join(current_dir, 'shortest.kv')
Builder.load_file(kv_file_path)

# IMPORTANT: ShortestPathScreen now inherits from Screen
class ShortestPathScreen(Screen):
    """
    The Python class for the Shortest Path Calculator screen.
    It extends Kivy's Screen class to be managed by a ScreenManager.
    """
    # Kivy property to update the result label dynamically from Python
    result_text = StringProperty("Select origin and destination to find the shortest path.")
    def go_back(self):
        """
        Navigates back to the previous screen in the ScreenManager history.
        """
        if self.manager:
            self.manager.current='dashboard'# Use go_back() to follow history

    def go_to_dashboard(self):
        """
        Navigates directly to the 'dashboard' screen.
        """
        if self.manager:
            self.manager.current = 'dashboard' # Set current screen by name
    def find_shortest(self):
        """
        Callback function for the 'Find Shortest Path' button.
        It retrieves selected origin, destination, mode, and traffic awareness,
        calls the dijkstra algorithm, and updates the UI with the results.
        """
        # Accessing widgets by ID works the same way
        start_node = self.ids.origin_spinner.text.strip()
        end_node = self.ids.destination_spinner.text.strip()
        selected_mode = self.ids.mode_spinner.text
        traffic_aware = self.ids.traffic_checkbox.active

        # Basic input validation
        if start_node == "Select Origin" or end_node == "Select Destination":
            self.result_text = "[color=ff0000]Please select both origin and destination.[/color]"
            return

        # Ensure the selected nodes exist in the city_map
        if start_node not in city_map or end_node not in city_map:
            self.result_text = "[color=ff0000]Invalid city selected. Please choose from the list defined in city_map.[/color]"
            return

        print(f"Finding shortest path from: {start_node} to {end_node}")
        print(f"Mode: {selected_mode}, Traffic Aware: {traffic_aware}")

        # Call the dijkstra algorithm
        path, total_value = dijkstra(start_node, end_node, mode=selected_mode, traffic_aware=traffic_aware)

        if total_value == float('inf'):
            self.result_text = f"[color=ff0000]No path found from {start_node} to {end_node}.[/color]"
        else:
            path_str = " -> ".join(path)
            unit = "km" if selected_mode == 'distance' else "minutes"
            self.result_text = (
                f"[b]Shortest Path:[/b] {path_str}\n"
                f"[b]Total {selected_mode.capitalize()}:[/b] {total_value:.2f} {unit}"
            )

