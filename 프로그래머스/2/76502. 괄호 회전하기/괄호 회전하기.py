from collections import deque

def solution(elements):
    answer = 0
    l = len(elements)
    elements = elements * 2
    
    for i in range(l):
        if check(elements[i:i+l]):
            answer += 1
    
    return answer


def check(s):
    s = deque(s)
    q = deque()
    q.append(s.popleft())
    
    while s:
        c = s.popleft()
        if c in '([{': q.append(c)
        elif c in ')]}':
            if not q: return False
            elif (c == ')' and q[-1] == '(') or (c == ']' and q[-1] == '[') or (c == '}' and q[-1] == '{'):
                q.pop()
    if q: return False
    return True