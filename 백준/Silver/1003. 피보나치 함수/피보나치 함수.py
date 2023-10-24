N = int(input())
for i in range(N):
    M = int(input())
    ls = [[1,0], [0,1]] + [[0,0] for _ in range(M-1)]
    if M < 2:
        print(ls[M][0], ls[M][1])
        continue
    for j in range(2, M+1):
        ls[j] = [ls[j-1][0] + ls[j-2][0], ls[j-1][1] + ls[j-2][1]]
    print(ls[M][0], ls[M][1])