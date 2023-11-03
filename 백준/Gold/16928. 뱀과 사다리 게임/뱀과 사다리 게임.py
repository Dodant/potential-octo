from collections import deque

N, M = map(int, input().split())
ladder = [list(map(int, input().split())) for _ in range(N+M)]

ladder = dict(ladder)
visited = [[False, 0] for _ in range(101)]

st = 1
q = deque()
q.append(st)

while q:
    cur = q.popleft()
    
    for i in range(1,7):
        np  = cur + i
        if np <= 100 and not visited[np][0]:
            if np in ladder.keys():
                np = ladder[np]
            
            if not visited[np][0]:
                q.append(np)
                visited[np][0] = True
                visited[np][1] = visited[cur][1] + 1
        
print(visited[100][1])