from collections import deque

N = int(input())
for case in range(N):
    M, B, K = map(int, input().split())
    ls = [[0 for _ in range(M)] for _ in range(B)]
    visited = [[False for _ in range(M)] for _ in range(B)]
    for i in range(K):
        x, y = map(int, input().split())
        ls[y][x] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    cnt = 2
    for i in range(B):
        for j in range(M):
            if ls[i][j] == 1 and not visited[i][j]:
                q = deque()
                q.append([i, j])
                
                while q:
                    cur = q.popleft()
                    if visited[cur[0]][cur[1]]: continue
                    visited[cur[0]][cur[1]] = True
                    ls[cur[0]][cur[1]] = cnt
                    
                    for k in range(4):
                        nx, ny = cur[0] + dx[k], cur[1] + dy[k]
                        if nx < 0 or nx >= B or ny < 0 or ny >= M: continue
                        if visited[nx][ny] or ls[nx][ny] == 0: continue
                        q.append([nx, ny])
                cnt += 1

    print(cnt-2)