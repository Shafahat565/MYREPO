from queue import Queue
import heapq
from itertools import product

# ----------------------------------
# Task 1: Search Algorithms
# ----------------------------------
campus_graph = {
    'Hostel': {'Cafeteria': 5, 'Lab': 10},
    'Cafeteria': {'Library': 4, 'Admin': 8},
    'Library': {'Classroom1': 2},
    'Lab': {'Classroom2': 3},
    'Admin': {'Classroom1': 6, 'Classroom2': 4},
    'Classroom1': {},
    'Classroom2': {}
}

def bfs(start, goal):
    visited = set()
    queue = Queue()
    queue.put((start, [start]))

    while not queue.empty():
        node, path = queue.get()
        if node == goal:
            return path, len(path)-1, (len(path)-1)*5
        visited.add(node)
        for neighbor in campus_graph[node]:
            if neighbor not in visited:
                queue.put((neighbor, path + [neighbor]))
    return None, 0, 0

def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path, len(path)-1, (len(path)-1)*5
        visited.add(node)
        for neighbor in campus_graph[node]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None, 0, 0

def a_star(start, goal):
    queue = [(0, start, [start], 0)]
    visited = set()

    while queue:
        _, node, path, cost = heapq.heappop(queue)
        if node == goal:
            return path, cost, cost * 2
        visited.add(node)
        for neighbor in campus_graph[node]:
            if neighbor not in visited:
                new_cost = cost + campus_graph[node][neighbor]
                heapq.heappush(queue, (new_cost, neighbor, path + [neighbor], new_cost))
    return None, 0, 0
if __name__ == "__main__":
    print("\n🔍 Task 1: Search Algorithms")
    print("BFS Path:", bfs('Hostel', 'Classroom1'))
    print("DFS Path:", dfs('Hostel', 'Classroom1'))
    print("A* Path :", a_star('Hostel', 'Classroom1'))
