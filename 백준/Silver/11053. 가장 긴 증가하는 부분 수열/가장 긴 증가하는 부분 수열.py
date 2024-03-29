n = int(input())
arr = list(map(int, input().split()))
arr1 = [0] * n

for i in range(1, len(arr)):
    idx_arr = []
    for j in range(0, i):
        if arr[i] > arr[j]:
            idx_arr.append(arr1[j])
    if len(idx_arr) == 0:
        continue
    arr1[i] = max(idx_arr) + 1
    
print(max(arr1)+1)