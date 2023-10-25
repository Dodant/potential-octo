from collections import deque
import copy
N = int(input())
paint = [list(map(str, input())) for _ in range(N)]
visited = [[False] * N for i in range(N)]
faint = copy.deepcopy(paint)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = deque()
cnt = 1
for i in range(N):
    for j in range(N):
        if visited[i][j]: continue
        q.append([i,j,cnt])
        color = paint[i][j]
        while q:
            cur = q.popleft()
            if visited[cur[0]][cur[1]]: continue
            if color != paint[cur[0]][cur[1]]: continue
            visited[cur[0]][cur[1]] = True
            paint[cur[0]][cur[1]] = cnt
            for k in range(4):
                nx, ny = cur[0] + dx[k], cur[1] + dy[k]
                if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                q.append([nx, ny, cnt])
        cnt += 1

q = deque()
cnt_ = 1

for i in range(N):
    for j in range(N):
        if faint[i][j] == 'G':
            faint[i][j] = 'R'
            
visited = [[False] * N for i in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j]: continue
        q.append([i,j,cnt_])
        color = faint[i][j]
        while q:
            cur = q.popleft()
            if visited[cur[0]][cur[1]]: continue
            if color != faint[cur[0]][cur[1]] : continue
            visited[cur[0]][cur[1]] = True
            faint[cur[0]][cur[1]] = cnt_
            for k in range(4):
                nx, ny = cur[0] + dx[k], cur[1] + dy[k]
                if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                q.append([nx, ny, cnt_])
        cnt_ += 1        

print(max(sum(paint, [])), max(sum(faint, [])))