cases = int(input())

for _ in range(cases):
    n = int(input())
    dp = [1, 1, 1, 2, 2]
    if n < 6:
        print(dp[n-1])
    else:
        for i in range(5, n):
            dp.append(dp[i-1] + dp[i-5])
        print(dp[-1])   