import heapq
import sys
input = sys.stdin.readline

absq = []
othe = dict()
heapq.heapify(absq)

N = int(input())
for i in range(N):
    M = int(input().rstrip())
    
    if M == 0:
        if not absq and 0 == sum(othe.values()):
            print(0)
        else:
            v = heapq.heappop(absq)
            if -v in othe and othe[-v] >= 1:
                print(-v)
                othe[-v] -= 1
            elif v in othe and othe[v] >= 1:
                print(v)
                othe[v] -= 1
    else:
        if M in othe: othe[M] += 1
        else: othe[M] = 1
        heapq.heappush(absq, abs(M))