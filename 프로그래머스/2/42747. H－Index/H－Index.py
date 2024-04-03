def solution(citations):
    answer = []
    citations.sort()
    
    for i in range(max(citations)+1):
        if i <= len([j for j in citations if i <= j]):
            answer.append(i)
        
    
    return max(answer)