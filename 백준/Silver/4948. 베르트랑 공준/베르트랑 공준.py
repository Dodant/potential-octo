ls = [False] * (123457 * 2)

for i in range(2, 123457 * 2):
    if ls[i]: continue
    for j in range(i+i, 123457 * 2, i):
        ls[j] = True

while True:
    n = int(input())
    if n == 0: break
    print(ls[n+1:2*n+1].count(False))