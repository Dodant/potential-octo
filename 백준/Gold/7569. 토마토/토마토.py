from collections import deque

N, M, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]

visited = [[[False] * N for j in range(M)] for i in range(H)]

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]

q = deque()

for i in range(H):
    for j in range(M):
        for k in range(N):
            if boxes[i][j][k] == 1:
                q.append([i,j,k,1])
                visited[i][j][k] = True
        
while q:
    z, x, y, cc = q.popleft()
    if boxes[z][x][y] == 1: pass
    elif boxes[z][x][y] == 0:
        visited[z][x][y] = True
        boxes[z][x][y] = cc
    else: continue
        
    for w in range(6):
        nz, nx, ny = z+dz[w], x+dx[w], y+dy[w]
        if nz < 0 or nx < 0 or ny < 0 or nz >= H or nx >= M or ny >= N: continue
        if not visited[nz][nx][ny]: q.append([nz,nx,ny,cc+1])

max_v = 0
flag = False
for i in range(H):
    for j in range(M):
        for k in range(N):
            if boxes[i][j][k] > max_v: max_v = boxes[i][j][k]
            if boxes[i][j][k] == 0:
                flag = True
                break
    if flag: break
if flag: print(-1)
else: print(max_v - 1)