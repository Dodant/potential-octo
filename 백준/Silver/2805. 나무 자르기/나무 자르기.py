N, M = map(int, input().split())
ls = list(map(int, input().split()))
# N, M = 4, 11
# ls = [1, 3, 3, 10]
st = 0
end = max(ls)

while st <= end:
    mid = (st + end) // 2
    cnt = 0
    for i in ls:
        if i > mid:
            cnt += i - mid
    if cnt >= M:
        st = mid + 1
    else:
        end = mid - 1
    
print(end)