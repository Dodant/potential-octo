n, m = map(int, input().split())
s = []

def dfs():
    if len(s) == m:
        print(*s)
        return 
    for i in range(1, n+1):
        s.append(i)
        if s == sorted(s):
            dfs()
            s.pop()
        else:
            s.pop()

dfs()