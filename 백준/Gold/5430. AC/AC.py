import sys
input = sys.stdin.readline


from collections import deque

T = int(input())

for i in range(T):
    p = input().rstrip()
    n = int(input().rstrip())
    ls = input().rstrip()
    
    if ls == '[]':
        ls = deque()
    else:
        ls = ls[1:-1]
        ls = deque(list(map(int, ls.split(','))))
    
    p.replace('RR', '')
    direction = True
    flag = False
    for j in p:
        if j == 'R': 
            direction = not direction
        elif j == 'D' and len(ls) == 0:
            print('error')
            flag = True
            break
        elif j == 'D' and direction:
            ls.popleft()
        elif j == 'D' and not direction:
            ls.pop()
            
    if not flag:
        if direction:
            print(f'[{",".join(map(str, ls))}]')
        else:
            print(f'[{",".join(map(str, reversed(ls)))}]')  