n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
dp = [[0]*n for i in range(n)]

dp[0][0] = board[0][0]
for i in range(1, n): dp[i][0] = dp[i-1][0] + board[i][0]
for j in range(1, n): dp[0][j] = dp[0][j-1] + board[0][j]
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + board[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

    if x1 == y1 == 0: print(dp[x2][y2])
    elif x1 == 0: print(dp[x2][y2] - dp[x2][y1-1])
    elif y1 == 0: print(dp[x2][y2] - dp[x1-1][y2])
    else: print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])