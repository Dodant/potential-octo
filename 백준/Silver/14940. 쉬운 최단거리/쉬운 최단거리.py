from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ls = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

st_point = [0, 0, 0]

for i in range(N):
    for j in range(M):
        if ls[i][j] == 2: st_point = [i, j, 0]
        if ls[i][j] == 1: ls[i][j] = -1

q = deque()
q.append(st_point)

while q:
    c = q.popleft()
    if visited[c[0]][c[1]]: continue
    visited[c[0]][c[1]] = True
    ls[c[0]][c[1]] = c[2]
    
    for i in range(4):
        nx, ny = c[0] + dx[i], c[1] + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if visited[nx][ny] or ls[nx][ny] == 0: continue
        q.append([nx, ny, c[2]+1])

for i in range(N):
    for j in range(M):
        print(ls[i][j], end=' ')
    print()