from kivy.uix.screenmanager import Screen
from traffic import get_traffic_status
from kivy.lang import Builder

Builder.load_file("screens/checktraffic.kv")

# ... your other imports ...
from kivy.uix.popup import Popup
from kivy.utils import get_color_from_hex

class CheckTrafficScreen(Screen):
    def __init__(self, **kwargs):
        super(CheckTrafficScreen, self).__init__(**kwargs)

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
            return  # Stop the rest of the function from executing

        # Placeholder traffic logic
        if origin == destination:
            message = "Origin and destination cannot be the same."
            color_box.background_color = get_color_from_hex("#FFFF00")
            text_label.text = "[b]Invalid Input[/b]"
        elif origin == "Thamel" and destination == "Baneshwor":
            message = "High traffic expected."
            color_box.background_color = get_color_from_hex("#FF0000")
            text_label.text = "[b]High Traffic[/b]"
        elif origin == "Lazimpat" and destination == "Baluwatar":
            message = "Medium traffic expected."
            color_box.background_color = get_color_from_hex("#FFFF00")
            text_label.text = "[b]Medium Traffic[/b]"
        else:
            message = "Low traffic expected."
            color_box.background_color = get_color_from_hex("#00FF00")
            text_label.text = "[b]Low Traffic[/b]"

        text_label.size_hint_x = None
        text_label.width = text_label.texture_size[0]
