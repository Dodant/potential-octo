import heapq 

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first >= K: return answer
        heapq.heappush(scoville, first + 2*second)
        answer += 1    
        if len(scoville) == 1 and scoville[0] >= K: 
            return answer
        if len(scoville) == 1: return -1