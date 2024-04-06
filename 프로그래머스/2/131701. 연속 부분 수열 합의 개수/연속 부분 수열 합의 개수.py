from collections import deque

def solution(elements):
    original = elements
    elements = deque(elements)
    numbers = set()
    l = len(elements)
    
    for i in range(1, l+1):
        elements = deque(original)
        for _ in range(l):
            numbers.add(sum(list(elements)[:i]))
            elements.append(elements.popleft())
        original = elements

    return len(numbers)