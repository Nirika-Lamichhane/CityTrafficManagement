from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from traffic_logic import get_traffic_status  # Use your own logic file name

Builder.load_file("screens/checktraffic.kv")

class CheckTrafficScreen(Screen):
    traffic_color = ListProperty([0.5, 0.5, 0.5, 1])  # Default grey
    route_path = StringProperty("")
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

    def set_box_color(self, hex_color):
        color = get_color_from_hex(hex_color)
        self.traffic_color = color

    def check_traffic(self):
        origin = self.ids.origin_spinner.text
        destination = self.ids.destination_spinner.text
        color_box = self.ids.traffic_color_box
        text_label = self.ids.traffic_text_label
        route_label = self.ids.route_path_label

        # Validation
        if origin == "Select Origin" or destination == "Select Destination":
            popup = Popup(title="Missing Information",
                          content=Label(text="Please select both Origin and Destination."),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            return

        if origin == destination:
            self.set_box_color("#FFFF00")  # Yellow
            text_label.text = "[b]Origin and destination cannot be the same[/b]"
            route_label.text = ""
            return

        # Get traffic data from logic
        traffic_data = get_traffic_status(origin, destination)
        traffic_level = traffic_data.get("traffic_level", "Unknown")
        main_route = traffic_data.get("route", [])
        alt_routes = traffic_data.get("alternative_routes", [])

        # Determine color and message for main traffic level
        if "high" in traffic_level.lower():
            color = "#FF0000"  # Red
            text_label.text = "[b]High Traffic[/b]"
        elif "medium" in traffic_level.lower():
            color = "#FFFF00"  # Yellow
            text_label.text = "[b]Medium Traffic[/b]"
        elif "low" in traffic_level.lower():
            color = "#00FF00"  # Green
            text_label.text = "[b]Low Traffic[/b]"
        else:
            color = "#808080"  # Grey
            text_label.text = f"[b]{traffic_level}[/b]"

        self.set_box_color(color)

        # Show route(s)
        route_display = f"[b]Main Route (shortest distance):[/b] {' -> '.join(main_route)}"

        # Only show alternative routes if traffic is high or medium
        if traffic_level.lower() in ["high", "medium"] and alt_routes:
            for alt in alt_routes:
                alt_path = " -> ".join(alt["route"])
                alt_level = alt["traffic_level"]
                alt_color = (
                    "[color=#FF0000]" if "high" in alt_level.lower()
                    else "[color=#FFFF00]" if "medium" in alt_level.lower()
                    else "[color=#00FF00]" if "low" in alt_level.lower()
                    else "[color=#808080]"
                )
                route_display += f"\n[b]Alternative Route (less traffic route):[/b] {alt_path} - {alt_color}{alt_level}[/color]"

        route_label.text = route_display
