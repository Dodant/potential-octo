n = int(input())

for i in range(n):
    x, y = 0, 0
    for j in range(9):
        q, w = map(int, input().split())
        x += q
        y += w
        
    if x > y:
        print("Yonsei")
    elif x < y:
        print("Korea")
    else:
        print("Draw")