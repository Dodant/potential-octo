n = int(input())
ls = list(map(int, input().split()))
s = int(input())

space = 0
for i in ls:
    if i == 0: continue
    if i < s: space += s
    elif i % s == 0: space += i
    else: space += ((i // s) + 1) * s
print(space)