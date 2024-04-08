import heapq

def solution(n, roads):
    answer = []
    graph = [[] for i in range(n+1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    dist = dijkstra(n, 1, graph)
    return dist.count(max(dist[1:]))


def dijkstra(n, start, graph):
    q = []
    distance = [1000000000] * (n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist: continue
        for b in graph[cur]:
            if dist + 1 < distance[b]:
                distance[b] = dist + 1
                heapq.heappush(q, (dist+1, b))
    return distance