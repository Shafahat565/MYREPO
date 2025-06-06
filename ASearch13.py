import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristics = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 0
}

def a_star_search(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start, [start]))  # (f = g+h, g, node, path)
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path

        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))
    
    return None

start = 'A'
goal = 'F'
path = a_star_search(graph, heuristics, start, goal)

if path:
    print("Path taken by A* to reach goal:", " -> ".join(path))
else:
    print("Goal not reachable from the start node.")
