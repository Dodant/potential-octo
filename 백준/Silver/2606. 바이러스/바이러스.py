from collections import deque

N = int(input())
M = int(input())
ls = [list(map(int, input().split())) for _ in range(M)]
gr = [[0 for _ in range(N)] for _ in range(N)]

for l, r in ls:
    gr[l-1][r-1] = 1
    gr[r-1][l-1] = 1

visited = [False for _ in range(N)]

q = deque()
q.append(0)

cnt = 0
while q:
    cur = q.popleft()
    if visited[cur]: continue
    visited[cur] = True
    cnt += 1
    for i in range(N):
        if gr[cur][i] == 1 and not visited[i]:
            q.append(i)
print(cnt-1)