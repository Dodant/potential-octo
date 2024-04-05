n, m = map(int, input().split())
ls = sorted(list(input().split()))
ols_s = []
s = []

for i in ls:
    while i in s:
        i = i + '*'
    s.append(i)

ls = s
s = []

set_ = set()

def dfs():
    if len(s) == m:
        set_.add(' '.join(list(map(str, s))).replace('*', ''))
        return 
    for i in ls:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()

new_list = []

for i in list(set_):
    new_list.append(list(map(int, i.split())))

for i in sorted(new_list):
    if i == sorted(i):
        print(*i)