from collections import deque

N, M = map(int, input().split())
q = deque()
q.append([N, 0])
bind = set()

if N > M:
    print(N-M)
else:
    while q:
        c = q.popleft()
        bind.add(c[0])
        if c[0] > 100001: continue
        if c[0] == M:
            print(c[1])
            break
        else:
            if c[0]+1 not in bind: q.append([c[0]+1, c[1]+1])
            if c[0]-1 not in bind: q.append([c[0]-1, c[1]+1])
            if c[0]*2 not in bind and c[0]*2 < 300001: q.append([c[0]*2, c[1]+1])