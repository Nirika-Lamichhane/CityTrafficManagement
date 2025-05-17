from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import Screen

from kivy.lang import Builder

Builder.load_file("screens/checktraffic.kv")

class CheckTrafficScreen(Screen):
    def check_traffic(self):
        origin = self.ids.origin_spinner.text
        destination = self.ids.destination_spinner.text
        color_box = self.ids.traffic_color_box
        text_label = self.ids.traffic_text_label

        if origin == "Select Origin" or destination == "Select Destination":
            popup = Popup(title="Missing Information",
                          content=Label(text="Please select both Origin and Destination."),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            return

        # Helper to update canvas color
        def set_box_color(color_hex):
            color_instruction = color_box.canvas.before.children[1]
            color_instruction.rgba = get_color_from_hex(color_hex)

        if origin == destination:
            message = "Origin and destination cannot be the same."
            set_box_color("#FFFF00")  # Yellow
            text_label.text = "[b]Invalid Input[/b]"
        elif origin == "Thamel" and destination == "Baneshwor":
            message = "High traffic expected."
            set_box_color("#FF0000")  # Red
            text_label.text = "[b]High Traffic[/b]"
        elif origin == "Lazimpat" and destination == "Baluwatar":
            message = "Medium traffic expected."
            set_box_color("#FFFF00")  # Yellow
            text_label.text = "[b]Medium Traffic[/b]"
        else:
            message = "Low traffic expected."
            set_box_color("#00FF00")  # Green
            text_label.text = "[b]Low Traffic[/b]"

        text_label.size_hint_x = None
        text_label.width = text_label.texture_size[0]
