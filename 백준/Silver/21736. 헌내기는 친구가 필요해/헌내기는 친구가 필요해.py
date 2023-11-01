from collections import deque

N, M = map(int, input().split())
mapp = [list(input()) for i in range(N)]

st = [0, 0]
visited = [[False] * M for i in range(N)]

for i in range(N):
    for j in range(M):
        if mapp[i][j] == 'I': st = [i, j]
        elif mapp[i][j] == 'X': visited[i][j] = True

q = deque()
q.append(st)
cnt = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]

while q:
    cur = q.popleft()
    if visited[cur[0]][cur[1]]: continue
    visited[cur[0]][cur[1]] = True
    if mapp[cur[0]][cur[1]] == 'P': cnt += 1
    
    for i in range(4):
        nx, ny = cur[0]+dx[i], cur[1]+dy[i]
        if 0 <= nx < N and 0 <= ny < M: 
            if not visited[nx][ny]: q.append([nx, ny])

if cnt == 0:
    print('TT')
else:
    print(cnt)
