N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0] = ls[0]

for i in range(1, N):
    dp[i][0] = ls[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = ls[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = ls[i][2] + min(dp[i-1][0], dp[i-1][1])
print(min(dp[-1]))