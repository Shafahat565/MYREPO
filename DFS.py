from collections import deque

def DFS(Start,Graph):
    Visited=set()
    stack=[Start]
    Visited.add(Start)
    size=0
    while stack:
        StartNode=stack.pop()
        print(StartNode,end="->")
        size+=1
        for neighbour in reversed(Graph[StartNode]):
            if neighbour not in Visited:
                Visited.add(neighbour)
                stack.append(neighbour)
    return size           
    
Graph={
    'A':['B','E','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':['B','D'],
    'F':[],
    'G':[],
}
print(DFS('A',Graph))