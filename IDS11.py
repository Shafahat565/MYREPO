graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dls(node, goal, depth, graph, visited):
    if depth == 0 and node == goal:
        return True
    if depth > 0:
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dls(neighbor, goal, depth - 1, graph, visited):
                    return True
    return False

def ids(graph, start_node, goal_node, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        if dls(start_node, goal_node, depth, graph, visited):
            return depth
    return -1

start = 'A'
goal = 'F'
max_depth = 5

found_depth = ids(graph, start, goal, max_depth)
if found_depth != -1:
    print(f"Goal node '{goal}' found at depth {found_depth}.")
else:
    print(f"Goal node '{goal}' not found within depth {max_depth}.")
