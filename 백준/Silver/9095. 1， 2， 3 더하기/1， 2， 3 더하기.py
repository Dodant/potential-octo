N = int(input())
for i in range(N):
    M = int(input())
    ls = [0, 1, 2, 4] + [0] * (M-3)
    if M < 4:
        print(ls[M])
        continue
    for j in range(4, M+1):
        ls[j] = ls[j-1] + ls[j-2] + ls[j-3]
    print(ls[M])