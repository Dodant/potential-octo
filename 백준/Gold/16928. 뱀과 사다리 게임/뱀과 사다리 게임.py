import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

# idx 위치에는 기본적으로 idx가 있음
# 다만 사다리나 뱀이 있는 경우는, 주사위 횟수 카운팅없이
# 끄트머리로 이동하므로, 그 끄트머리의 next_idx 값을
# idx 위치에 넣어놓아줌. 카운팅은 같으면서 동일 칸 취급
board = [i for i in range(101)]
visited = [0]*101

for _ in range(N):
    x, y = map(int, input().split())
    board[x] = y
    
for _ in range(M):
    u, v = map(int, input().split())
    board[u] = v

def BFS(start):
    q = deque([start])
    
    while q:
        x = q.popleft()
        
        for nx in range(x+1, x+7):
            if nx > 100:
                continue
            
            # 뱀이나 사다리가 없으면 nx 그대로고, 있다면
            # 그 끄트머리 번호 저장
            cnt = board[nx]
            
            if visited[cnt] == 0:
                visited[cnt] = visited[x] + 1
                q.append(cnt)
                
                if cnt == 100:
                    return visited[100]
            
    return False
                
print(BFS(1))