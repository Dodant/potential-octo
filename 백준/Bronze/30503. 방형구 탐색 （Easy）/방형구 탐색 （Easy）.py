import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    q = input().split()
    if q[0] == '1':
        l = int(q[1])
        r = int(q[2])
        k = int(q[3])
        print(ls[l-1:r].count(k))
    else:
        l = int(q[1])
        r = int(q[2])
        ls[l-1:r] = [0] * (r-l+1)