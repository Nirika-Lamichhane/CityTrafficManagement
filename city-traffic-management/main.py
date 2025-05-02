import heapq  # imports heap queue i.e. priority queue to get the smallest distance
from city_map import city_map

def dijkstra(start, end, mode='distance'):
    distances = {node: float('inf') for node in city_map}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()
    previous = {node: None for node in city_map}

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == end:
            break

        for neighbor, (time, distance) in city_map[current_node]:
            weight = distance if mode == 'distance' else time
            total = current_distance + weight
            if total < distances[neighbor]:
                distances[neighbor] = total
                previous[neighbor] = current_node
                heapq.heappush(pq, (total, neighbor))

    # Reconstruct path
    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous[current]

    return path, distances[end]

if __name__ == "__main__":
    # this line makes this code snippet under this run only when it is called directly from this file but not imported
    
    print("Available cities:", ", ".join(city_map.keys()))
    start_node = input("Enter starting location: ")
    end_node = input("Enter destination: ")
    mode = input("Optimize for 'distance' or 'time': ").lower()

    if start_node in city_map and end_node in city_map:
        path, cost = dijkstra(start_node, end_node, mode)
        print(f"\nShortest path from {start_node} to {end_node}:")
        print(" -> ".join(path))
        print(f"Total {mode}: {round(cost, 2)} {'km' if mode == 'distance' else 'minutes'}")
    else:
        print("Invalid city names entered.")
