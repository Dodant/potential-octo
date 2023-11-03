from collections import deque

T = int(input())

for _ in range(T):
    start, target = map(int, input().split())

    q = deque()
    q.append((start, ''))
    bb = set()
    bb.add(start)

    while q:
        cur, cmd = q.popleft()

        if cur == target:
            print(cmd)
            break
        
        d_cur = (2*cur)%10000
        if d_cur not in bb: 
            q.append((d_cur, cmd+'D'))
            bb.add(d_cur)
        
        if cur == 0:
            s_cur = 9999
        else:
            s_cur = cur - 1
        if s_cur not in bb: 
            q.append((s_cur, cmd+'S'))
            bb.add(s_cur)
        
        if len(str(cur)) == 1:
            r_cur = '000' + str(cur)
        elif len(str(cur)) == 2:
            r_cur = '00' + str(cur)
        elif len(str(cur)) == 3:
            r_cur = '0' + str(cur) 
        else:
            r_cur = str(cur)
        r_cur = r_cur[-1] + r_cur[:-1]
        r_cur = int(r_cur)
        if r_cur not in bb: 
            q.append((r_cur, cmd+'R'))
            bb.add(r_cur)
    
        if len(str(cur)) in [1, 2, 3]:
            if cur*10 not in bb:
                q.append((cur*10, cmd+'L'))
                bb.add(cur*10)
        else:
            l_cur = str(cur)
            l_cur = l_cur[1:] + l_cur[0]
            l_cur = int(l_cur)
            if l_cur not in bb:
                q.append((l_cur, cmd+'L'))
                bb.add(l_cur)
