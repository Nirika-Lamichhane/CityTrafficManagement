import random
import requests

use_real_api=False

def get_mock_traffic_status(origin,destination):
    traffic_levels=["low","medium","high"]   
    traffic=random.choices(traffic_levels,weights=[0.4,0.4,0.2])[0]
    
    return {
    "origin": origin,
    "destination": destination,
    "traffic_level": traffic
   }
'''
here weights haru le chai low medioum high ko probabilty dine ho kun chai ranfom le kasari select garca vabera
ani [0] le chai hamlai value chaine ho list haina so esle chai output lai value ko rup ma dekhauxa not list so used
k=1 use gareni hunx anagareni as specify nagareni random le euta item nai choose garxa


'''

# real api call structure
def get_real_traffic_status(origin, destination):
    api_key="Your API KEY"
    url="https://maps.googleapis.com/maps/api/directions/json?"
    params={
        "origin": origin,
        "destination": destination,
        "key": api_key
    }

    try:
        # Make the API call to Google Maps Directions API
        response = requests.get(url, params=params)
        data = response.json()
        
        if data["status"] == "OK":
            # Extract the estimated travel time (ETA)
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

# ✅ Unified Traffic Status Function (mock or real)
def get_traffic_status(origin, destination):
    if use_real_api:
        return get_real_traffic_status(origin, destination)
    else:
        return get_mock_traffic_status(origin, destination)