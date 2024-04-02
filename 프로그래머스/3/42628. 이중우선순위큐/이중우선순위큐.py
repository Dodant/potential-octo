import heapq

def solution(operations):
    min_heap = []
    
    for i in operations:
        if i == 'D 1':
            if len(min_heap) == 0: continue
            min_heap = heapq.nlargest(len(min_heap), min_heap)[1:]
            heapq.heapify(min_heap)
        elif i == 'D -1':
            if len(min_heap) == 0: continue
            heapq.heappop(min_heap)
        else:
            num = int(i.split()[-1])
            heapq.heappush(min_heap, num)

    if min_heap:
        return [max(min_heap), min(min_heap)]
    else:
        return [0,0]