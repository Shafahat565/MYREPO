from collections import deque

def BFS(Start,Graph):
    Visited=set()
    queue=deque([Start])
    Visited.add(Start)
    size=0
    while queue:
        StartNode=queue.popleft()
        print(StartNode,end="->")
        size+=1
        for neighbour in Graph[StartNode]:
            if neighbour not in Visited:
                Visited.add(neighbour)
                queue.append(neighbour)
    return size           
    
Graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':['G','H'],
    'E':[],
    'F':[],
    'G':[],
    'H':[]
}
print(BFS('B',Graph))