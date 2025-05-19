import random
import requests
from dijkstra import dijkstra
from city_map import city_map

use_real_api = False

def get_mock_traffic_status(origin, destination, intermediate=None):
    traffic_levels = ["low", "medium", "high"]
    traffic = random.choices(traffic_levels, weights=[0.4, 0.4, 0.2])[0]

    if intermediate:
        path1, dist1 = dijkstra(origin, intermediate)
        path2, dist2 = dijkstra(intermediate, destination)
        full_route = path1 + path2[1:]  # combine paths, avoid duplicate node
    else:
        full_route, dist = dijkstra(origin, destination)

    return {
        "origin": origin,
        "destination": destination,
        "traffic_level": traffic,
        "route": full_route,
    }

def get_real_traffic_status(origin, destination):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
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

            # Extract steps to generate a route
            steps = data["routes"][0]["legs"][0]["steps"]
            route = [step["html_instructions"] for step in steps]

            return {
                "origin": origin,
                "destination": destination,
                "traffic_level": f"Real-time (ETA: {duration})",
                "route": route,
            }
        else:
            return {
                "origin": origin,
                "destination": destination,
                "traffic_level": "unknown (API error)",
                "route": [origin, destination],
            }
    except Exception as e:
        return {
            "origin": origin,
            "destination": destination,
            "traffic_level": f"error: {str(e)}",
            "route": [origin, destination],
        }

def get_traffic_status(origin, destination, intermediate=None):
    if use_real_api:
        return get_real_traffic_status(origin, destination)
    else:
        return get_mock_traffic_status(origin, destination, intermediate)
