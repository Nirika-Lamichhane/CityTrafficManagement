# defining city and routes as a graph here cities are in nodes and distance will be the edges
# each item represents a node in graph i.e. every locations

city_map = {
    "Thamel": [("Lazimpat", (5, 0.4)), ("Dilli Bazaar", (8, 0.6))],
    "Lazimpat": [("Thamel", (5, 0.4)), ("Baluwatar", (6, 0.5))],
    "Baluwatar": [("Lazimpat", (6, 0.5)), ("Gairidhara", (4, 0.3))],
    "Baneshwor": [("Dilli Bazaar", (7, 0.8)), ("Chabahil", (10, 1.2))],
    "Dilli Bazaar": [("Thamel", (8, 0.7)), ("Baneshwor", (7, 0.8))],
    "Gairidhara": [("Baluwatar", (4, 0.3)), ("Boudha", (9, 1.0))],
    "Boudha": [("Gairidhara", (9, 1.0)), ("Chabahil", (6, 0.5))],
    "Chabahil": [("Boudha", (6, 0.5)), ("Baneshwor", (10, 1.2))],
    "Patan": [("Baneshwor", (11, 1.5)), ("Kalimati", (9, 1.1))],
    "Kalimati": [("Patan", (9, 1.1)), ("Thamel", (12, 1.3))]
}

# city map is a dictionary where each key is a city eg thamel lazimpat of the lhs side and the value is a list of tuples i.e. after =
# tuple is in the form of minutes and distance in km

'''
accessing the distance and time of the route
time,distance=city_map["Thamel"][0][1] ; this returns 1st tuple ko 2nd part i.e. time distance part of the first city i.e. 0th index of thamel


print("Time:",time)
print("Distance:",distance)
here yo list of dict ho kinaki esle dict lai [] ma rakhxa ani hamle
dict lai change garna mildainaa i.e. non  mutable ho dict but list is mutable
so list ma convert gareko


'''