
from functools import reduce
# import sys
# input = sys.stdin.readline

case = int(input())
for _ in range(case):
    dc = dict()
    n = int(input())
    for j in range(n):
        _, kind = input().split()
        if kind in dc:
            dc[kind] += 1
        else:
            dc[kind] = 1
    for i in dc:
        dc[i] += 1
    answer = 1
    for i in dc.values():
        answer *= i
    print(answer-1)