from collections import deque


N, M = map(int, input().split())
ls = [[i for i in input().strip()] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append([0, 0, 1])
out = False
while q:
    cur = q.popleft()
    if visited[cur[0]][cur[1]]:
        continue
    visited[cur[0]][cur[1]] = True
    for i in range(4):
        nx, ny = cur[0] + dx[i], cur[1] + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if visited[nx][ny] or ls[nx][ny] == '0': continue
        q.append([nx, ny, cur[2]+1])
        if nx == N-1 and ny == M-1:
            print(cur[2]+1)
            out = True
            break
    if out:
        break