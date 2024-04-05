n, m = map(int, input().split())
ls = sorted(list(map(int, input().split())))
set_ = []
s = []

def dfs():
    if len(s) == m:
        lss = ' '.join(list(map(str, s)))
        if lss not in set_:
            set_.append(lss)
            print(lss)
        return 
    for i in ls:
        s.append(i)
        if s == sorted(s):
            dfs()
        s.pop()

dfs()