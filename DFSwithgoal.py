from collections import deque

def DFS(Start,End,Graph):
    Visited=set()
    stack=[Start]
    Visited.add(Start)
    size=0
    while stack:
        StartNode=stack.pop()
        print(StartNode,end="->")
        if(StartNode==End):
            break
        size+=1
        for neighbour in reversed(Graph[StartNode]):
            if neighbour not in Visited:
                Visited.add(neighbour)
                stack.append(neighbour)
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
print(DFS('D','C',Graph))