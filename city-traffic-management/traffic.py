import random
import requests

use_real_api=False

def get_mock_traffic_status(origin,destination):
    traffic_levels=["low","medium","high"]   
    traffic=random.choice(traffic_levels,weights=[0.4,0.4,0.2])[0]
    
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