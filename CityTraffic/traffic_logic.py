import random
import requests

use_real_api = False

def get_mock_traffic_status(origin, destination):
    traffic_levels = ["low", "medium", "high"]
    traffic = random.choices(traffic_levels, weights=[0.4, 0.4, 0.2])[0]
    return {
        "origin": origin,
        "destination": destination,
        "traffic_level": traffic
    }

def get_real_traffic_status(origin, destination):
    api_key = "Your API KEY"
    url = "https://maps.googleapis.com/maps/api/directions/json?"
    params = {
        "origin": origin,
        "destination": destination,
        "key": api_key
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        if data["status"] == "OK":
            duration = data["routes"][0]["legs"][0]["duration"]["text"]
            return {
                "origin": origin,
                "destination": destination,
                "traffic_level": f"Real-time (ETA: {duration})"
            }
        else:
            return {
                "origin": origin,
                "destination": destination,
                "traffic_level": "unknown (API error)"
            }
    except Exception as e:
        return {
            "origin": origin,
            "destination": destination,
            "traffic_level": f"error: {str(e)}"
        }

def get_traffic_status(origin, destination):
    if use_real_api:
        return get_real_traffic_status(origin, destination)
    else:
        return get_mock_traffic_status(origin, destination)
