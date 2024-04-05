n = int(input())
ls = list(input().split())
s = []
new_ls = []
answer = 0

for i in ls:
    while i in new_ls: i = i +'*'
    new_ls.append(i)

def check(s):
    answer_ = 0
    for i in range(len(s)-1):
        a = int(s[i].replace('*',''))
        b = int(s[i+1].replace('*',''))
        answer_ += abs(a-b)
    return answer_

def dfs():
    global answer
    if len(s) == n:
        answer = max(answer, check(s))
        return
    for i in new_ls:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
        
dfs()
print(answer)
