n, m = map(int, input().split())
ls = sorted(list(map(int, input().split())))
s = []

def dfs():
    if len(s) == m:
        print(*s)
        return 
    for i in ls:
        s.append(i)
        if s == sorted(s):
            dfs()
        s.pop()

dfs()