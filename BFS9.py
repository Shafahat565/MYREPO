from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            traversal_order.append(node)
            visited.add(node)
            queue.extend(graph[node])
    
    return traversal_order

start = 'A'
order = bfs(graph, start)
print("BFS Traversal starting from node", start, "is:", " -> ".join(order))
