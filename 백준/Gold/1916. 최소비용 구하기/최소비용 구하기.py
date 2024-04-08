import heapq


n = int(input())
m = int(input())

distance = [1000000000000] * (n+1)
board = [[1000000000000]*(n+1) for i in range(n+1)]
graph = [[] for i in range(n+1)]
dupl_check = set()

for i in range(m):
    a, b, c = map(int, input().split())
    board[a][b] = min(board[a][b], c)
    dupl_check.add((a, b))
    
for a, b in dupl_check:
    graph[a].append((b, board[a][b]))    
    
start, target = map(int, input().split())

def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist: continue
        for node, cost in graph[cur]:
            if dist + cost < distance[node]:
                distance[node] = dist + cost
                heapq.heappush(q, (dist+cost, node))

dijkstra(start)
print(distance[target])