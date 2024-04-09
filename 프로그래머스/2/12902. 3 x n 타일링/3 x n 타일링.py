def solution(n):
    if (n+1) % 2 == 0: return 0
        
    dp = [0, 3, 0, 11]
    for i in range(5, n, 2):
        dp.append(0)
        dp.append((dp[i-2]*3+2*sum(dp[:-3])+2) % 1_000_000_007)

    return dp[n-1]