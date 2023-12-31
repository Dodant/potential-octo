dct = {}

def w(a, b, c):
    if (a, b, c) in dct: 
        return dct[(a, b, c)]
    
    if a <= 0 or b <= 0 or c <= 0: 
        return 1
    
    if a > 20 or b > 20 or c > 20: 
        return w(20, 20, 20)
    
    if a < b and b < c: 
        if (a, b, c-1) not in dct: dct[(a, b, c-1)] = w(a, b, c-1)
        if (a, b-1, c-1) not in dct: dct[(a, b-1, c-1)] = w(a, b-1, c-1)
        if (a, b-1, c) not in dct: dct[(a, b-1, c)] = w(a, b-1, c)
        return dct[(a, b, c-1)] + dct[(a, b-1, c-1)] - dct[(a, b-1, c)]
        
    if (a-1, b, c) not in dct: dct[(a-1, b, c)] = w(a-1, b, c)
    if (a-1, b-1, c) not in dct: dct[(a-1, b-1, c)] = w(a-1, b-1, c)
    if (a-1, b, c-1) not in dct: dct[(a-1, b, c-1)] = w(a-1, b, c-1)
    if (a-1, b-1, c-1) not in dct: dct[(a-1, b-1, c-1)] = w(a-1, b-1, c-1)

    return dct[(a-1, b, c)] + dct[(a-1, b-1, c)] + dct[(a-1, b, c-1)] - dct[(a-1, b-1, c-1)]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1: break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')