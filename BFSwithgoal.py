from collections import deque

def BFS(Start,End,Graph):
    Visited=set()
    queue=deque([Start])
    Visited.add(Start)
    size=0
    while queue:
        StartNode=queue.popleft()
        print(StartNode,end="->")
        if(StartNode==End):
            break
        size+=1
        for neighbour in Graph[StartNode]:
            if neighbour not in Visited:
                Visited.add(neighbour)
                queue.append(neighbour)
    return size           

Graph={
    'A':['B','E','C'],
    'B':['D','E','A'],
    'C':['A','F','G'],
    'D':['B','E'],
    'E':['A','B','D'], 
    'F':['C'],
    'G':['C'],
}
print(BFS('D','C',Graph))