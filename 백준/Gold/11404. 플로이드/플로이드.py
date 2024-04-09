n = int(input())
m = int(input())
# graph = [[0]*(n+1) for i in range(n+1)]
dist = [[1000000000000]*(n+1) for i in range(n+1)]
for i in range(m): 
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
    
for i in range(n+1): 
    dist[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(0 if dist[i][j] == 1000000000000 else dist[i][j], end=' ')
    print()