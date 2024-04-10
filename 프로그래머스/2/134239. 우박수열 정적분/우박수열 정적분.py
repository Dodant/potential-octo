def solution(k, ranges):
    answer = []
    k_ls = [k]
    dp = []
    
    while k != 1:
        if k % 2 == 0:
            k //= 2
            k_ls.append(k)
        else:
            k = k * 3 + 1
            k_ls.append(k)
    
    for i in range(1, len(k_ls)):
        dp.append((k_ls[i] + k_ls[i-1])/2)
    n = len(dp)
    for i in ranges:
        if i == [0,0]: answer.append(sum(dp))
        elif i[0] > n+i[1]: answer.append(-1.0)
        else: answer.append(sum(dp[i[0]:n+i[1]]))

    return answer

print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))
print(solution(3, [[0,0], [1,-2], [3,-3]]))