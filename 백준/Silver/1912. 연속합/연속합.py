n = int(input())
ls = list(map(int, input().split()))
dp = [-99999 for _ in range(n)]
dp[0] = ls[0]
for i in range(1, n):
    sum_ = dp[i-1] + ls[i]
    dp[i] = max(sum_, ls[i])
print(max(dp))