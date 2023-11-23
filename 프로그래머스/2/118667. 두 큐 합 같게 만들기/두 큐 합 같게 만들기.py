from collections import deque

def solution(queue1, queue2):
    answer = -2
    length = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    
    sum1, sum2 = sum(queue1), sum(queue2)
    answer = 0
    while sum1 != sum2:
        if sum1 > sum2:
            s = queue1.popleft()
            queue2.append(s)
            sum1 -= s
            sum2 += s
            answer += 1
        elif sum1 < sum2:
            s = queue2.popleft()
            queue1.append(s)
            sum1 += s
            sum2 -= s
            answer += 1
        if answer > length * 3 + 1:
            return -1
            
    return answer
