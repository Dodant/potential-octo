from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)
            
def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in sorted(graph[now]):
            if not visited[i]:
                q.append(i)
                visited[i] = True
    

N, M, V = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]  
visited = [False for _ in range(N+1)]

for u, v in ls:
    graph[u].append(v)
    graph[v].append(u)
dfs(graph, V, visited)
print()
visited = [False for _ in range(N+1)]
bfs(graph, V, visited)