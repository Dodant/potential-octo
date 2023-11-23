
from itertools import combinations, permutations

def check(user, bann):
    if len(user) != len(bann):
        return False
    for i in range(len(bann)):
        if bann[i] == '*': continue
        if user[i] != bann[i]: return False
    return True
        
def solution(user_id, banned_id):
    answer = 0
    total = []
    for i in permutations(user_id, len(banned_id)):
        ls = list(i)
        mn = list(i)
        for j in banned_id:
            lls = [k for k in ls if check(k, j)]
            if len(lls) == 0: continue
            ls.remove(lls[0])
        ls.sort()
        if len(ls) == 0:
            total.append(mn)
    
    answer = set()
    
    for j in total:
        answer.add(str(sorted(j)))
    
    return len(answer)