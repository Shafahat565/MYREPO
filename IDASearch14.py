
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 3)],
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

def ida_star(start, goal):
    threshold = heuristics[start]
    path = [start]

    while True:
        temp = search(path, 0, threshold, goal)
        if isinstance(temp, list):
            return temp
        if temp == float('inf'):
            return None
        threshold = temp

def search(path, g, threshold, goal):
    node = path[-1]
    f = g + heuristics[node]

    if f > threshold:
        return f
    if node == goal:
        return path

    min_threshold = float('inf')

    for neighbor, cost in graph.get(node, []):
        if neighbor not in path:
            path.append(neighbor)
            temp = search(path, g + cost, threshold, goal)
            if isinstance(temp, list):
                return temp
            if temp < min_threshold:
                min_threshold = temp
            path.pop()

    return min_threshold


start_node = 'A'
goal_node = 'F'
path = ida_star(start_node, goal_node)

if path:
    total_cost = 0
    for i in range(len(path) - 1):
        for neighbor, cost in graph[path[i]]:
            if neighbor == path[i + 1]:
                total_cost += cost
                break
    print("Path found by IDA*:", " -> ".join(path))
    print("Total cost:", total_cost)
else:
    print("Goal not reachable from the start node.")
