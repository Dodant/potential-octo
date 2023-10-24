from collections import deque

N = int(input())
ls = [[int(i) for i in input()] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 2
for i in range(N):
    for j in range(N):
        if ls[i][j] == 1 and not visited[i][j]:
            q = deque()
            q.append([i, j])
            
            while q:
                cur = q.popleft()
                if visited[cur[0]][cur[1]]: continue
                visited[cur[0]][cur[1]] = True
                ls[cur[0]][cur[1]] = cnt
                
                for k in range(4):
                    nx, ny= cur[0] + dx[k], cur[1] + dy[k]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                    if visited[nx][ny] or ls[nx][ny] == 0: continue
                    q.append([nx, ny])
            cnt += 1

print(cnt-2)
answer = [0] * (cnt-2)

for i in range(N):
    for j in range(N):
        if ls[i][j] != 0:
            answer[ls[i][j]-2] += 1
print('\n'.join(map(str, sorted(answer))))