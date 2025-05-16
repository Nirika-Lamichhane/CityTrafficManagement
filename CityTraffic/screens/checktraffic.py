from kivy.uix.screenmanager import Screen
from traffic import get_traffic_status
from kivy.lang import Builder

Builder.load_file("screens/checktraffic.kv")


class CheckTrafficScreen(Screen):
   def check_traffic(self):
    origin = self.ids.origin_spinner.text
    destination = self.ids.destination_spinner.text

    if origin != "Select Origin" and destination != "Select Destination":
        result = get_traffic_status(origin, destination)
        self.ids.content_label.text = (
            f"Traffic from {result['origin']} to {result['destination']} is {result['traffic_level']}"
        )
        self.ids.origin_spinner.text = "Select Origin"
        self.ids.destination_spinner.text = "Select Destination"
    else:
        self.ids.content_label.text = "Please select both origin and destination."
