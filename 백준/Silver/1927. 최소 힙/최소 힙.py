import heapq
import sys
input = sys.stdin.readline

minq = []
heapq.heapify(minq)

N = int(input())
for i in range(N):
    M = int(input().rstrip())
    if M == 0:
        if not minq:
            print(0)
        else:
            print(heapq.heappop(minq))
    else:
        heapq.heappush(minq, M)