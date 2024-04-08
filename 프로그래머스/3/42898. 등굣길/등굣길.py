def solution(m, n, puddles):
    answer = 0
    new_pud = []
    for i, j in puddles:
        print([j-1, i-1])
        new_pud.append([j-1, i-1])
        
    dp = [[0]*m for i in range(n)]
    for i in range(n): dp[i][0] = 1
    for j in range(m): dp[0][j] = 1
    for i, j in new_pud: dp[i][j] = 0

    for i, j in new_pud:
        if i == 0 and j != 0: 
            for k in range(j, m): dp[i][k] = 0
        if j == 0 and i != 0:
            for k in range(i, n): dp[k][j] = 0

    
    for nn in range(1, n):
        for mm in range(1, m):
            if [nn, mm] in new_pud: continue
            dp[nn][mm] = (dp[nn-1][mm] + dp[nn][mm-1]) % 1_000_000_007

    
    return dp[n-1][m-1]