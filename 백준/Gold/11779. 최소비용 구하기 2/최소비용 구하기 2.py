import heapq


n = int(input())
m = int(input())
# n, m = 5, 8
distance = [1000000000000000] * (n+1)
board = [[1000000000000000]*(n+1) for i in range(n+1)]
graph = [[] for i in range(n+1)]
dupl_check = set()

for i in range(m):
    a, b, c = map(int, input().split())
    if a == b: continue
    board[a][b] = min(board[a][b], c)
    dupl_check.add((a, b))
    
for a, b in dupl_check:
    graph[a].append((b, board[a][b]))    
    
start, target = map(int, input().split())
# start, target = 1, 5
loads = [[start] for i in range(n+1)]
# graph = [[], [(2, 2), (5, 10), (4, 1), (3, 3)], [(4, 2)], [(4, 1), (5, 1)], [(5, 3)], []]

def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist: continue
        for node, cost in graph[cur]:
        
            if dist + cost < distance[node]:
                loads[node] = loads[cur] + [node]
                distance[node] = dist + cost
                heapq.heappush(q, (dist+cost, node))
                

dijkstra(start)
print(distance[target])
print(len(loads[target]))
print(*loads[target])