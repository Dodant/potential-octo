from collections import deque

def solution(rc, operations):
    left = deque()
    center = deque()
    right = deque()
    
    for i in range(len(rc)):
        center.append(deque(rc[i][1:-1]))
        left.append(rc[i][0])
        right.append(rc[i][-1])
        
    for i in operations:
        if i == "Rotate":
            if len(rc[0]) == 2:
                left, center, right = rotate_2(left, center, right)
            else:
                left, center, right = rotate(left, center, right)
        elif i == "ShiftRow":
            left, center, right = shift_row(left, center, right)

    answer = []
    for i in range(len(rc)):
        ls = []
        ls.append(left.popleft())
        ls.extend(center[i])
        ls.append(right.popleft())
        answer.append(ls)
        
    return answer

def shift_row(left, center, right):
    left.appendleft(left.pop())
    center.appendleft(center.pop())
    right.appendleft(right.pop())
    return left, center, right

def rotate(left, center, right):
    center[0].appendleft(left.popleft())
    right.appendleft(center[0].pop())
    left.append(center[-1].popleft())
    center[-1].append(right.pop())
    return left, center, right

def rotate_2(left, center, right):
    right.appendleft(left.popleft())
    left.append(right.pop())
    return left, center, right