from collections import deque

def dfs(graph, v, visited, parents):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            parents[i] = parents[v]
            dfs(graph, i, visited, parents)

def solution(n, wires):
    vvv = []
    wires = deque(wires)
    for i in range(len(wires)):
        left = wires.popleft()
        graph = [[] for _ in range(n)]
        for j in wires:
            graph[j[0]-1].append(j[1]-1)
            graph[j[1]-1].append(j[0]-1)
            
        parents = [i for i in range(n)]
        visited = [False for _ in range(n)]
        
        for k in range(0, n):
            if not visited[k]:
                dfs(graph, k, visited, parents)
                
        vvv.append(abs(parents.count(list(set(parents))[0]) - parents.count(list(set(parents))[1])))
        wires.append(left)
    return min(vvv)