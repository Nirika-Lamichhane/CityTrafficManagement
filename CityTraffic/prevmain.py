import heapq  # imports heap queue i.e. priority queue to get the smallest distance
from city_map import city_map
from traffic import get_traffic_status
from plyer import notification  # for desktop notifications
# plyer is library and notification is the module

import tkinter as tk
from tkinter import messagebox,ttk
import threading
import time
import random

notifications_enabled =False # jist used simply to not use the certain portions of the code without commentiong or deleting it




# -----------------------Notifications---------------------
def background_notification():
    while notifications_enabled:
        origin,destination=random.sample(list(city_map.keys()),2)
        '''
        choice is used to select only 1 item from the list and not many 
        so sample is used to select 2 items not repeating itself from the list
        '''
        status=get_traffic_status(origin, destination)['traffic_level']
        '''
        this line is used to get the traffic level i.e. this one key value pair from the 
        dict 
        '''
        notification.notify(
            title=f"Traffic update from {origin}->{destination} ",
            message=f"Traffic from {origin} to {destination}: {status}",
            timeout=10 
             # Notification duration in seconds
        )
        '''
        notification is an object or module depending on how it is imported
        notify is method of that object
        methods are like functions but they are associated with the object
        () this is used to call the method and pass the parameters to it
        : is used to define the functions and methods in python

        '''
        time.sleep(7200) # Sleep for 2 hours (7200 seconds)


def start_notification_thread():
    thread=threading.Thread(target=background_notification,daemon=True)
    thread.start()

# ------------------ GUI -------------------
def check_traffic():
    origin = start_var.get()
    destination = end_var.get()
    mode = mode_var.get()

    if origin == destination:
        result_var.set("Start and destination must be different.")
        return

    if origin in city_map and destination in city_map:
        path, cost = dijkstra(origin, destination, mode)
        traffic = get_traffic_status(origin, destination)['traffic_level']
        result = f"Path: {' ➝ '.join(path)}\nTotal {mode}: {round(cost, 2)} {'km' if mode == 'distance' else 'min'}\nTraffic: {traffic}"
        result_var.set(result)
    else:
        result_var.set("Invalid city selection.")

def ask_notification_permission():
    global notifications_enabled
    answer = messagebox.askyesno("Allow Notifications", "Do you want to receive automatic traffic alerts?")
    notifications_enabled = answer
    if answer:
        start_notification_thread()

# ------------------ MAIN WINDOW -------------------
root = tk.Tk()
root.title("City Traffic Management")
root.geometry("400x300")

# Dropdowns
cities = list(city_map.keys())
start_var = tk.StringVar(value=cities[0])
end_var = tk.StringVar(value=cities[1])
mode_var = tk.StringVar(value='distance')

ttk.Label(root, text="Start Location:").pack()
ttk.OptionMenu(root, start_var, start_var.get(), *cities).pack()

ttk.Label(root, text="Destination:").pack()
ttk.OptionMenu(root, end_var, end_var.get(), *cities).pack()

ttk.Label(root, text="Optimize by:").pack()
ttk.OptionMenu(root, mode_var, 'distance', 'distance', 'time').pack()

ttk.Button(root, text="Check Traffic", command=check_traffic).pack(pady=10)

result_var = tk.StringVar()
ttk.Label(root, textvariable=result_var, wraplength=380).pack(pady=5)

# Ask for permission after GUI loads
root.after(1000, ask_notification_permission)

root.mainloop()



if __name__ == "__main__":
    # this line makes this code snippet under this run only when it is called directly from this file but not imported
    
    print("Available cities:", ", ".join(city_map.keys()))
    start_node = input("Enter starting location: ").title()
    end_node = input("Enter destination: ").title()
    mode = input("Optimize for 'distance' or 'time': ").lower()
    
    if start_node == end_node:
        print("start and end locations are the same.")
    elif start_node in city_map and end_node in city_map:
        path, cost = dijkstra(start_node, end_node, mode)
        print(f"\nShortest path from {start_node} to {end_node}:")
        print(" -> ".join(path))
        print(f"Total {mode}: {round(cost, 2)} {'km' if mode == 'distance' else 'minutes'}")

        # calling traffic function
        traffic_status = get_traffic_status(start_node, end_node)
        print(f"Traffic status from {start_node} to {end_node}: {traffic_status['traffic_level']}")
    else:
        print("Invalid city names entered.")
