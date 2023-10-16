A, B, C = map(int, input().split())

def power(a, b):
    if b % 2 == 0:
        if b == 0:
            return 1
        else:
            return power(a, b//2) ** 2 % C
    else:
        if b == 1:
            return a
        else:
            return power(a, b//2) ** 2 * a % C
        
print(power(A, B)%C)