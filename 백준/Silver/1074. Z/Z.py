N, r, c = map(int, input().split())

def check(N, r, c):
    if N == 0:
        return 0
    if N == 1:
        if r == 0 and c == 0: return 0
        elif r == 0 and c == 1: return 1
        elif r == 1 and c == 0: return 2
        else: return 3
    else:
        if r < 2**(N-1) and c < 2**(N-1):
            return check(N-1, r, c)
        elif r < 2**(N-1) and c >= 2**(N-1):
            return check(N-1, r, c-2**(N-1)) + 2**(2*(N-1))
        elif r >= 2**(N-1) and c < 2**(N-1):
            return check(N-1, r-2**(N-1), c) + 2**(2*(N-1)) * 2
        else:
            return check(N-1, r-2**(N-1), c-2**(N-1)) + 2**(2*(N-1)) * 3
        
print(check(N, r, c))