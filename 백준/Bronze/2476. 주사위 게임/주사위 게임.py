n = int(input())
ls = []
for _ in range(n):
    x, y, z = map(int, input().split())
    if x == y == z:
        ls.append(10000+x*1000)
    elif x == y or x == z:
        ls.append(1000+x*100)
    elif z == y:
        ls.append(1000+y*100)
    else:
        c = max(x,y,z)
        ls.append(c*100)
print(max(ls))