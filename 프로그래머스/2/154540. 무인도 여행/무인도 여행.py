from collections import deque
import sys 
sys.setrecursionlimit(10000)

def solution(maps):
    answer = []
    h, w = len(maps), len(maps[0])
    
    global new_map
    new_map = []
    
    global visited
    visited = [[True] * w for _ in range(h)]
    
    global island
    island = deque()
    
    for i in range(h):
        row = []
        for j in range(w):
            if maps[i][j] == 'X':
                row.append(0)
            else:
                row.append(int(maps[i][j]))
                visited[i][j] = False
                island.append((i,j))
        new_map.append(row)

    while island:
        x, y = island.popleft()
        if visited[x][y]: continue
        answer.append(dfs(x, y, h, w))
        
    if not answer: return [-1]
    return sorted(answer)
    
def dfs(x, y, h, w):
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    if 0 <= x < h and 0 <= y < w and not visited[x][y]:
        area = new_map[x][y]
        visited[x][y] = True
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
            area += dfs(nx, ny, h, w)
        return area
    else: 
        return 0
        