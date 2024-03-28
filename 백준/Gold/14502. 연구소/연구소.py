from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]

virus_queue = deque()

for i in range(n):
    graph.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2: 
            virus_queue.append((i,j))

def bfs():
    virus_temp_queue = deque()
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2: 
                virus_temp_queue.append((i,j))
                
    tmp_graph = copy.deepcopy(graph)
    
    while virus_temp_queue:
        x, y = virus_temp_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    virus_temp_queue.append((nx, ny))
    global answer
    cnt = sum(tmp_graph, []).count(0)
    answer = max(answer, cnt)
    
def make_wall(count):
    if count == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count + 1)
                graph[i][j] = 0

answer = 0
make_wall(0)
print(answer)