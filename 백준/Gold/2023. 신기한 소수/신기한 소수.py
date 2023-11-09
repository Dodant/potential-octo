N = int(input())
        
def is_prime_number(x):
    if x == 1: return False
    if x == 2: return True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: return False
    return True

def backtracking(candi, N):
    if len(candi) == N:
        print(candi)
        return
    else:
        for i in range(1, 10, 2):
            cani = candi + str(i)
            if is_prime_number(int(cani)):
                backtracking(cani, N)

for i in ['2','3','5','7']:
    backtracking(i, N)