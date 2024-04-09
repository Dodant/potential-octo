from collections import deque

def solution(maps):

    n, m = len(maps), len(maps[0])
    q = deque([(0,0)])
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    visited = [[False] * m for i in range(n)]
    dist = [[0] * m for i in range(n)]
    dist[0][0] = 1
    visited[0][0] = True
    
    if maps[n-1][m-2] == 0 and maps[n-2][m-1] == 0: return -1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: 
                if visited[nx][ny] or maps[nx][ny] == 0: continue
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))
                
    return dist[n-1][m-1] if dist[n-1][m-1] else -1