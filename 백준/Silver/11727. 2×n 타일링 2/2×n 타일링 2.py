N = int(input())
ls = [1,3,5] + [0] * (N-3)
if N < 3:
    print(ls[N-1])
else:
    for i in range(3, N):
        ls[i] = ls[i-1] + 2 * ls[i-2]
    print(ls[N-1] % 10007)