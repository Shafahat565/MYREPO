def DLS(start, goal, graph, limit, path):
    path.append(start)
    if start == goal:
        return True, path
    if limit <= 0:
        path.pop()
        return False, path
    for neighbour in graph.get(start, []):
        found, result_path = DLS(neighbour, goal, graph, limit - 1, path)
        if found:
            return True, result_path
    path.pop()
    return False, path

def IDS(start, goal, graph, max_depth):
    for depth in range(max_depth + 1):
        found, path = DLS(start, goal, graph, depth, [])
        if found:
            print("Path found:", ' -|> '.join(path))
            return path
    print("Not Found")
    return []

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G']
}

IDS('A', 'G', graph, 3)
