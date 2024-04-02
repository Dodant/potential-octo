from collections import deque

def solution(order):
    len_order = len(order)
    order = deque(order)
    boxes = deque(list(range(1, len_order+1)))
    bojo_ = deque()
    answer = 0

    while True:
        if len(boxes) != 0 and order[0] == boxes[0]:
            boxes.popleft()
            order.popleft()
            answer += 1
        elif len(bojo_) != 0 and order[0] == bojo_[0]:
            bojo_.popleft()
            order.popleft()
            answer += 1
        elif len(boxes) != 0:
            bojo_.appendleft(boxes.popleft())
        else:
            return answer