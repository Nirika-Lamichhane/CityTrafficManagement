from city_map import city_map
import heapq

# Traffic penalty function (used only when traffic_aware=True)
def get_weight(time, distance, traffic_level):
    traffic_penalty = {
        "low": 0,
        "medium": 2,
        "high": 5
    }
    return distance + traffic_penalty[traffic_level]

def dijkstra(start, end, mode='distance', traffic_aware=False):
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

        for neighbor, data in city_map.get(current_node, []):
            # Compatibility: data could be (time, dist) or (time, dist, traffic)
            if traffic_aware and len(data) == 3:
                time, distance, traffic_level = data
                weight = get_weight(time, distance, traffic_level)
            else:
                time, distance = data[:2]
                weight = distance if mode == 'distance' else time

            total = current_distance + weight
            if total < distances[neighbor]:
                distances[neighbor] = total
                previous[neighbor] = current_node
                heapq.heappush(pq, (total, neighbor))

    # Check if destination reachable
    if distances[end] == float('inf'):
        return [], float('inf')  # No path found

    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous[current]

    return path, distances[end]
