graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, start_node):
    visited = set()
    traversal_order = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            traversal_order.append(node)
            visited.add(node)
            stack.extend(reversed(graph[node]))
    
    return traversal_order

start = 'A'
order = dfs(graph, start)
print("DFS Traversal starting from node", start, "is:", " -> ".join(order))
