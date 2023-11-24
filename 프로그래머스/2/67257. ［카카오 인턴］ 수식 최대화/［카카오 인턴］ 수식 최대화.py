from itertools import combinations, permutations
from collections import deque

def solution(expression):
    answer = []
    operators = []
    if '+' in expression: operators.append('+')
    if '-' in expression: operators.append('-')
    if '*' in expression: operators.append('*')
    
    for i in permutations(operators, len(operators)):
        to_num_list = to_num(expression)
        for j in i:
            to_num_list = compute(to_num_list, j)
        answer.append(abs(to_num_list[0]))
    return max(answer)

def to_num(expression):
    q = deque()
    new_exp = []
    
    for i in expression:
        if i in ['+','-','*']:
            str_num = ''
            while q: str_num += q.popleft()
            new_exp.append(int(str_num))
            new_exp.append(i)
        else:
            q.append(i)
    str_num = ''
    while q: str_num += q.popleft()
    new_exp.append(int(str_num))
    return new_exp

def compute(to_num_list, operator):
    while operator in to_num_list:
        idx = to_num_list.index(operator)
        to_num_list[idx-1:idx+2] = [eval(f'{to_num_list[idx-1]}{operator}{to_num_list[idx+1]}')]
    return to_num_list
