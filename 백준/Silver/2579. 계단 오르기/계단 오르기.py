N = int(input())
ls = [0] + [int(input()) for i in range(N)]
# ls = [0] + list(map(int, input().split()))

if N == 1:
    print(ls[1])
elif N == 2:
    print(ls[1] + ls[2])
elif N == 3:
    print(max(ls[1] + ls[3], ls[2] + ls[3]))
else:
    dp = [0] * (N+1)
    dp[0] = 0
    dp[1] = ls[1]
    dp[2] = ls[1] + ls[2]
    dp[3] = max(ls[1] + ls[3], ls[2] + ls[3])
    for i in range(4, N+1):
        dp[i] = max(dp[i-3] + ls[i-1], dp[i-2]) + ls[i]
    print(dp[-1])