from collections import deque

cases = int(input())
for i in range(cases):
    L = int(input())
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))

    visited = [[0]*L for _ in range(L)]

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    def bfs(start, target):
        q = deque([start])

        while q:
            x, y = q.popleft()
            if x == target[0] and y == target[1]:
                return visited[x][y]
            else:
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < L and 0 <= ny < L and not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                        
    print(bfs(start, target))