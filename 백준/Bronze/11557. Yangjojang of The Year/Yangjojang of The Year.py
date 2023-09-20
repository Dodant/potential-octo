T = int(input())

for i in range(T):
    n, q = '', 0
    for j in range(int(input())):
        nn, qq = input().split()
        qq = int(qq)
        if qq > q:
            q = qq
            n = nn
    print(n)