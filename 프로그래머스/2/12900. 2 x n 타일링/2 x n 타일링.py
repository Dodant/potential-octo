def solution(n):
    dp = [1,2]
    for i in range(2, n):
        dp.append((dp[i-2]+dp[i-1]) % 1_000_000_007)

    return dp[-1]