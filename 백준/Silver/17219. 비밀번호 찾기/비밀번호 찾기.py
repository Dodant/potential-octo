N, M = map(int, input().split())
site = dict()
for i in range(N):
    s, p = input().split()
    site[s] = p
for i in range(M):
    print(site[input()])