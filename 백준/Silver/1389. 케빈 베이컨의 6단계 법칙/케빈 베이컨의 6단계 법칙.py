N, M = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(M)]
graph = [[10000] * N for i in range(N)]

for i in ls:
    x, y = i[0]-1, i[1]-1
    graph[x][y] = 1
    graph[y][x] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

ls = []
for i in range(N):
    ls.append((i+1, sum(graph[i])-graph[i][i]))
ls.sort(key=lambda x: x[1])
print(ls[0][0])