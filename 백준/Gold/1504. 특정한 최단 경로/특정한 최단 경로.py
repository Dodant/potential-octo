import heapq

n, m = map(int, input().split())
# n, m = 4, 5
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))    
    graph[b].append((a, c))
u, v = map(int, input().split())
# graph = [[], [(2, 3), (3, 1), (4, 1)], [(1, 3), (3, 3)], [(1, 1), (2, 3), (4, 4)], [(1, 1), (3, 4)]]

# u, v = 2, 3


def dijkstra(n, start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance = [1000000] * (n+1)
    distance[start] = 0
    
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist: continue
        for node, cost in graph[cur]:
            if dist + cost < distance[node]:
                distance[node] = dist + cost
                heapq.heappush(q, (dist+cost, node))
    if distance[end] != 1000000:
        if distance[end] == 0: return True, 0
        return True, distance[end]
    return False, 0

q, a = dijkstra(n, 1, u)
w, b = dijkstra(n, u, v)
e, c = dijkstra(n, v, n)
r, a1 = dijkstra(n, 1, v)
t, b1 = dijkstra(n, v, u)
y, c1 = dijkstra(n, u, n)
# print(a, b, c, a1, b1, c1)


if (q and w and e) and (r and t and y): 
    print(min(a + b + c, a1 + b1 + c1))
elif (q and w and e) and not (r and t and y):
    print(a+b+c)
elif not (q and w and e) and (r and t and y):
    print(a1+b1+c1)
else:
    print(-1)