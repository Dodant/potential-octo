M, N = map(int, input().split())
che = [False, False] + [True] * (N-1)

for i in range(2, int(N**0.5)+1):
    if che[i]:
        for j in range(2*i, N+1, i):
            che[j] = False

for i in range(M, N+1):
    if che[i]:
        print(i)