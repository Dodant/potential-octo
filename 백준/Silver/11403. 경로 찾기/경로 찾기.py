N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# N = 7
# graph = [[0,0,0,1,0,0,0],
#          [0,0,0,0,0,0,1],
#          [0,0,0,0,0,0,0],
#          [0,0,0,0,1,1,0],
#          [1,0,0,0,0,0,0],
#          [0,0,0,0,0,0,1],
#          [0,0,1,0,0,0,0]]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] != 0 and graph[k][j] != 0:
                graph[i][j] = graph[i][k]+graph[k][j]

for i in range(N):
    for j in range(N):
        print(1 if graph[i][j] != 0 else 0, end=' ')
    print()
        