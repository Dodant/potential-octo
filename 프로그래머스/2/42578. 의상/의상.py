from functools import reduce

def solution(clothes):
    answer = 0
    cloth_dict = {}
    for _, cate in clothes:
        cloth_dict[cate] = cloth_dict.get(cate, 1) + 1
    count = list(cloth_dict.values())    
    return reduce(lambda x, y: x*y, count) - 1