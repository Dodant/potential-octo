n, m = map(int, input().split())
arr = []
for i in range(1, m+1): arr.extend([i]*i)
print(sum(arr[n-1:m]))