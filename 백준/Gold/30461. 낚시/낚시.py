import sys
input = sys.stdin.readline

N, M, Q = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]

for x in range(1, N):
    for y in range(M):
        graph[x][y] += graph[x-1][y]

for x in range(1, N):
    for y in range(1, M):
        graph[x][y] += graph[x-1][y-1]

for i in range(Q):
    a, b = map(int, input().rstrip().split())
    print(graph[a-1][b-1])