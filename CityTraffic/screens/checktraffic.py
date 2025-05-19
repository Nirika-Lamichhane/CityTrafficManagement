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
            route_label.text = ""  # Clear any previous route
            return

        # Get traffic data
        traffic_data = get_traffic_status(origin, destination)
        traffic_level = traffic_data["traffic_level"]
        route = traffic_data.get("route", [])

        # Set UI elements based on traffic level
        if "high" in traffic_level.lower():
            color = "#FF0000"  # Red
            text = "[b]High Traffic[/b]"
        elif "medium" in traffic_level.lower():
            color = "#FFFF00"  # Yellow
            text = "[b]Medium Traffic[/b]"
        elif "low" in traffic_level.lower():
            color = "#00FF00"  # Green
            text = "[b]Low Traffic[/b]"
        else:
            color = "#808080"  # Grey
            text = f"[b]{traffic_level}[/b]"

        self.set_box_color(color)
        text_label.text = text

        if route:
            route_label.text = f"[b]Route:[/b] {' -> '.join(route)}"
        else:
            route_label.text = "" # Clear the route label if no route is available

    def set_box_color(self, color_hex):
        color_box = self.ids.traffic_color_box
        for instr in color_box.canvas.before.children:
            if hasattr(instr, 'rgba'):
                instr.rgba = get_color_from_hex(color_hex)
                break

