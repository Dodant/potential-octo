from itertools import combinations

N, M, R = map(int, input().split())
bar = list(map(int, input().split()))
flg = list(map(int, input().split()))
flg.sort()

def binary_search(ls, start, end, flr):
    mid = (start + end) // 2
    if start > end:
        return flr * 0.5 * ls[mid]
    elif flr * 0.5 * ls[mid] > R:
        return binary_search(ls, start, mid-1, flr)
    elif flr * 0.5 * ls[mid] < R:
        return binary_search(ls, mid+1, end, flr)
    else:
        return flr * 0.5 * ls[mid]

max_val = 0
for i in combinations(bar, 2): 
    area = binary_search(flg, 0, len(flg)-1, abs(i[0]-i[1]))
    if area > R: continue
    if area > max_val: max_val = area

if max_val == 0:
    print(-1)
else:
    print(f'{max_val:0.1f}')