def solution(k, dungeons):
    answer = 0
    order = []
    
    def dfs(answer, dungeons):
        max_cnt = answer
        if len(order) == len(dungeons):
            return max(answer, check(k, order, dungeons))

        for i in range(len(dungeons)):
            if i not in order:
                order.append(i)
                max_cnt = max(max_cnt, dfs(answer, dungeons))
                order.pop()
            
        return max_cnt
    return dfs(answer, dungeons)
    
def check(k, order, dungeons):
    count = 0
    for i in order:
        minimum, cost = dungeons[i]
        if k >= minimum:
            k -= cost
            count += 1
    return count