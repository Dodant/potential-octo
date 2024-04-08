import heapq

n, m = map(int, input().split())
start = int(input())
distance = [1000000] * (n+1)
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))    

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
for i in distance[1:]:
    if i == 1000000:
        print('INF')
    else:
        print(i)