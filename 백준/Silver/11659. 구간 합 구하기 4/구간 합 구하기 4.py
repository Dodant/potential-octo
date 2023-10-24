import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ls = list(map(int, input().rstrip().split()))

for i in range(1, N):
    ls[i] += ls[i-1]
for i in range(M):
    a, b = map(int, input().rstrip().split())
    if a == 1:
        print(ls[b-1])
    else:
        print(ls[b-1] - ls[a-2])
        