name = input()
n = int(input())
candi = [input() for _ in range(n)]
from itertools import combinations
from functools import reduce

candi_score = []

for cand_name in candi:
    count_arr = []
    
    for letter in 'LOVE':
        count_arr.append(cand_name.count(letter) + name.count(letter))
        
    combi_arr = []
    for a, b in combinations(count_arr, 2):
        combi_arr.append(a+b)
    candi_score.append((cand_name, reduce(lambda x, y: x*y, combi_arr) % 100))
    
print(sorted(candi_score, key= lambda x : (-x[1], x[0]))[0][0])