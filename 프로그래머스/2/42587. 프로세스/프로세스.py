from collections import deque

def solution(priorities, location):
    cnt = 0
    q = deque(priorities)
    c = deque([i for i in range(len(priorities))])
    t = []
    
    while q:
        if q[0] == max(q):
            cnt += 1
            q.popleft()
            a = c.popleft()
            t.append(a)
            
        else:
            q.append(q.popleft())
            c.append(c.popleft())
            
    return t.index(location) + 1

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))