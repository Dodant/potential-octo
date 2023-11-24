from collections import deque

def check(p):
    q = deque()
    p = deque(list(p))
    while p:
        c = p.popleft()
        if c == '(':
            q.append(c)
        elif c == ')':
            if len(q) == 0: return False
            else: q.pop()
    if len(q) != 0: return False
    return True
    
def splituv(p):
    for i in range(2, len(p)+1, 2):
        if p[0:i].count('(') == p[0:i].count(')') and p[i:].count('(') == p[i:].count(')'):
            return p[0:i], p[i:]
        
        
def solution(p):
    if check(p): return p
    if p == '': return ''
    
    u, v = splituv(p)
    if check(u): return u + solution(v)
    elif not check(u):
        uls = ''
        for i in u[1:-1]:
            if i == '(': uls += ')'
            elif i == ')': uls += '('       
        return '(' + solution(v) + ')' + uls