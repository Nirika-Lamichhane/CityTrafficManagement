import heapq  # imports heap queue i.e. priority queue i.e. used to allow us to access the smallest and largest distance during the search
from city_map import city_map

def dijkstra(start, end):
    distances = {node: float('inf') for node in city_map}  # Initialize distances to infinity
    distances[start] = 0  # Start node distance is 0
    pq = [(0, start)]  # Priority queue initialized with the start node (distance, node)
    visited = set()  # Set to track visited nodes
    previous = {node: None for node in city_map}  # Dictionary to keep track of the previous node in the shortest path
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)  # Pop the node with the smallest distance

        if current_node in visited:  # Skip if the node has already been visited
            continue
        visited.add(current_node)

        if current_node == end:  # If we reach the end node, stop the algorithm
            break

        # Loop through the neighbors of the current node
        for neighbor, weight in city_map[current_node].items():
            distance = current_distance + weight  # Calculate new distance to the neighbor

            # If the new distance is shorter, update the distance and push to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))  # Push the neighbor with the updated distance to the priority queue
