from itertools import permutations

def is_prime(num):
    if num in [0,1]: return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False 
    return True

def solution(numbers):
    answer = set()
    num_set = set()
    for n in range(1, len(numbers)+1):
        for i in permutations(numbers, n):
            num = int(''.join(list(i)))
            print(num)
            if num in num_set: continue
            if is_prime(num): answer.add(num)
    return len(answer)