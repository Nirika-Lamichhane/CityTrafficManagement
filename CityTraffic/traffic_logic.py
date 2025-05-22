import random
import requests
from dijkstra import dijkstra
from city_map import city_map

use_real_api = False

def get_mock_traffic_status(origin, destination, intermediate=None):
    traffic_levels = ["low", "medium", "high"]
    traffic = random.choices(traffic_levels, weights=[0.4, 0.4, 0.2])[0]

    # Main route
    if intermediate:
        path1, dist1 = dijkstra(origin, intermediate)
        path2, dist2 = dijkstra(intermediate, destination)
        main_route = path1 + path2[1:]
    else:
        main_route, dist = dijkstra(origin, destination)

    result = {
        "origin": origin,
        "destination": destination,
        "traffic_level": traffic,
        "route": main_route,
        "alternative_routes": []
    }

    # Generate alternative routes only if traffic is high or medium
    if traffic =="high":
        all_nodes = list(city_map.keys())
        if origin in all_nodes:
            all_nodes.remove(origin)
        if destination in all_nodes:
            all_nodes.remove(destination)

        alternatives = []
        low_traffic_alts = []
        used_intermediates = set()

        for _ in range(10):  # Try more times to get 4 good routes
            alt_intermediate = random.choice(all_nodes)
            if alt_intermediate in used_intermediates:
                continue
            used_intermediates.add(alt_intermediate)

            try:
                alt_path1, _ = dijkstra(origin, alt_intermediate)
                alt_path2, _ = dijkstra(alt_intermediate, destination)

                # Ensure valid path
                if not alt_path1 or not alt_path2:
                    continue
                if alt_path1[0] != origin or alt_path2[0] != alt_intermediate:
                    continue

                alt_route = alt_path1 + alt_path2[1:]

                # Avoid duplicates or loops
                if (
                    alt_route != main_route
                    and not any(alt_route.count(node) > 1 for node in alt_route)
                ):
                    alt_traffic = random.choice(traffic_levels)
                    if alt_traffic=="low":
                        low_traffic_alts.append(
                            {"route": alt_route, "traffic_level": alt_traffic}
                        )
    

            except Exception:
                continue

        # Add up to 2 low and 2 other alternative route
        result["alternative_routes"] = low_traffic_alts[:2]

    return result

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
