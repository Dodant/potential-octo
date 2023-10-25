import heapq
import sys
input = sys.stdin.readline

maxq = []
heapq.heapify(maxq)

N = int(input())
for i in range(N):
    M = -int(input().rstrip())
    if M == 0:
        if not maxq:
            print(0)
        else:
            print(-heapq.heappop(maxq))
    else:
        heapq.heappush(maxq, M)