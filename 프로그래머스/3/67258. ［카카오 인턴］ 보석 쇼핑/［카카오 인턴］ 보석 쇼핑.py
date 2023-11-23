def solution(gems):
    answer = [0, len(gems)]
    leng = len(set(gems))
    left, right = 0, 0
    gem_dict = {gems[0]: 1}
    
    while left < len(gems) and right < len(gems):
        if len(gem_dict) == leng:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            else:
                gem_dict[gems[left]] -= 1
                if gem_dict[gems[left]] == 0: del gem_dict[gems[left]]
                left += 1
                
        else:
            right += 1
            if right == len(gems): break
            gem_dict[gems[right]] = gem_dict.get(gems[right], 0) + 1
    
    return [answer[0]+1, answer[1]+1]