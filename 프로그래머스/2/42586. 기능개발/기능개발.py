from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        progresses = add_arr(progresses, speeds)
        count = 0
        while progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
            if not progresses:
                return answer + [count]
        answer.append(count)
    return answer

def add_arr(progresses, speeds):
    while progresses[0] < 100:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
    return progresses