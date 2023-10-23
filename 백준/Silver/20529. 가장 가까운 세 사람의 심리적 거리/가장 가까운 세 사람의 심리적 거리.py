T = int(input())

def dist(x, y):
    answer = 0
    if x[0] != y[0]:
        answer += 1
    if x[1] != y[1]:
        answer += 1
    if x[2] != y[2]:
        answer += 1
    if x[3] != y[3]:
        answer += 1
    return answer


def dist2(x,y,z):
    return dist(x,y) + dist(y,z) + dist(z,x)

from itertools import combinations

for i in range(T):
    N = int(input())
    ls = list(input().split())
    flag = False
    dct = {}
    two_list = []
    
    for j in ls:
        if j in dct:
            dct[j] += 1
        else:
            dct[j] = 1

    for i in dct:
        if dct[i] >= 3:
            print(0)
            flag = True
            break
        if dct[i] == 2:
            two_list.append(i)
    if flag:
        continue
    
    lls = list(set(ls))
    ds = []

    for i in two_list:
        for j in dct:
            if i == j:
                continue
            else:
                ds.append(2 * dist(i, j))

    for j in combinations(lls, 3):
        ds.append(dist2(*j))
    print(min(ds))