from collections import deque

def solution(n, computers):
    q = deque()
    visited = [0] * n
    visited_idx = 1
    
    for i in range(n):
        q.append(i)
        while q:
            idx = q.popleft()
            if visited[idx] != 0: continue
            else: visited[idx] = visited_idx
            
            for ix, item in enumerate(computers[idx]):
                if item == 0: continue
                if visited[ix] != 0: continue
                else:
                    q.append(ix)
        visited_idx += 1
                
    return len(set(visited))