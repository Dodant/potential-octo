from collections import deque
import heapq

def plus_ten(time):
    hh, mm = map(int, time.split(':'))
    if mm + 10 >= 60: 
        mm -= 50
        hh += 1
    else:
        mm += 10
    return f'{hh:02}:{mm:02}'

def solution(book_time):

    q = []
    book_time = deque(sorted(book_time))
    first = book_time.popleft()
    heapq.heappush(q, plus_ten(first[1]))
    answer = 1
    
    while book_time:
        starttime, endtime = book_time.popleft()
        fast_end_time = heapq.heappop(q)
        print(fast_end_time, starttime, endtime)
        if fast_end_time <= starttime:
            heapq.heappush(q, plus_ten(endtime))
        else:
            heapq.heappush(q, plus_ten(endtime))
            heapq.heappush(q, fast_end_time)
            answer += 1

    return answer