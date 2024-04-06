from collections import deque

def solution(elements):
    l = len(elements)
    elements = elements * 2
    numbers = set()
    
    for i in range(l):
        for j in range(i, l+i):
            numbers.add(sum(elements[i:j+1]))
    # print(numbers)
    return len(numbers)
