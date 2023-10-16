N = int(input())
ls = [[0] for _ in range(N)]
for i in range(N):
    ls[i] = list(map(int, input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = ls[0][0]

for i in range(1, N):
    for j in range(i+1):
        dp[i][j] = ls[i][j] + max(dp[i-1][j-1], dp[i-1][j])
        
print(max(dp[-1]))