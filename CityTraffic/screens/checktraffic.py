from kivy.uix.screenmanager import Screen
from traffic import get_traffic_status
from kivy.lang import Builder

Builder.load_file("screens/checktraffic.kv")


class CheckTrafficScreen(Screen):
    def check_traffic(self):
        origin=self.ids.origin_input.text
        destination=self.ids.destination_input.text

        if origin and destination:
            result=get_traffic_status(origin, destination)
            self.ids.result_label.text=f"Traffic from {result['origin']} to {result['destination']} is {result['traffic_level']}"
            self.ids.origin_input.text=""
            self.ids.destination_input.text=""
        else:
            self.ids.result_label.text="Please enter both origin and destination."
