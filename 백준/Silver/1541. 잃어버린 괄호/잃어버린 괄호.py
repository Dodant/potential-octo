string = input()
ls = string.split('-')
answer = 0

if '+' in ls[0]:
    lss = ls[0].split('+')
    for i in range(len(lss)):
        answer += int(lss[i])
else:
    answer += int(ls[0])

for i in range(1, len(ls)):
    v = 0
    if '+' in ls[i]:
        lss = ls[i].split('+')
        for j in range(len(lss)):
            v += int(lss[j])
        answer -= v
    else:
        answer -= int(ls[i])
        
print(answer)