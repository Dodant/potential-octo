import sys

def find_k(M, N, x, y):
    k = x
    while k <= M * N:
        if (k-x) % M == 0 and (k-y) % N == 0:
            return k
        k += M
    return -1

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())

    print(find_k(m, n, x, y))