n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
# n, m = 4, 3
# board = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
dp = [[0]*n for i in range(n)]
dp[0][0] = board[0][0]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0: continue
        elif i == 0 and j != 0: dp[i][j] = dp[i][j-1] + board[i][j]
        elif j == 0 and i != 0: dp[i][j] = dp[i-1][j] + board[i][j]
        else: dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + board[i][j]

# for i in range(n):
#     print(*dp[i])

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    # print(dp[x2][y2], dp[x1-1][y2], dp[x2][y1-1], dp[x1-1][y1-1])
    # print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
    if x1 == y1 == 0: print(dp[x2][y2])
    elif x1 == 0: print(dp[x2][y2] - dp[x2][y1-1])
    elif y1 == 0: print(dp[x2][y2] - dp[x1-1][y2])
    else: print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])