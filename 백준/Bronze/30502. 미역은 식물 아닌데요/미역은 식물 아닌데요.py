N, M = map(int, input().split())
ls = [[-2, -2] for _ in range(N)]

for i in range(M):
    a, b, c = input().split()
    a = int(a)-1
    if b == 'P' and c == '1':
        ls[a][0] = 1
    elif b == 'P' and c == '0':
        ls[a][0] = -1
    elif b == 'M' and c == '0':
        ls[a][1] = 1
    elif b == 'M' and c == '1':
        ls[a][1] = -1

answer_0 = 0
answer_1 = 0
for i in ls:
    if i[0] == 1 and i[1] == 1: 
        answer_0 += 1
        answer_1 += 1
        continue
    if i[0] == -2 and i[1] == -2: 
        answer_1 += 1
        continue
    if i[0] == -2 and i[1] == 1: 
        answer_1 += 1
        continue
    if i[0] == 1 and i[1] == -2: 
        answer_1 += 1
        continue
    
print(answer_0, answer_1)
