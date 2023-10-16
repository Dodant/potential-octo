from collections import deque
a, b = map(int,input().split())
q = deque()
q.append((a,1))

while q:
    n, t = q.popleft()
    if n == b:
        print(t)
        break
    else:
        if n*2 <= b:
            q.append((n*2, t+1))
        if int(str(n)+'1') <= b:
            q.append((int(str(n)+'1'), t+1))
else:
    print(-1)