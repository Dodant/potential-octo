n, m = map(int, input().split())
s = []

def dfs():
    if len(s) == m and s == sorted(s):
        print(*s)
        return 
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
            
dfs()
