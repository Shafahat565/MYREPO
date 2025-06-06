import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristics = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

def greedy_best_first_search(graph, heuristics, start, goal):
    visited = set()
    queue = []
    heapq.heappush(queue, (heuristics[start], start))
    path = []

    while queue:
        _, current = heapq.heappop(queue)
        if current not in visited:
            path.append(current)
            visited.add(current)

            if current == goal:
                return path

            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (heuristics[neighbor], neighbor))
    
    return None

start = 'A'
goal = 'F'
path = greedy_best_first_search(graph, heuristics, start, goal)

if path:
    print("Path taken to reach goal:", " -> ".join(path))
else:
    print("Goal not reachable from the start node.")
