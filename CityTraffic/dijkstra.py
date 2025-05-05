from city_map import city_map
import heapq  # imports heap queue i.e. priority queue to get the smallest distance



# -----------------------dijkistra algorithm---------------------

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