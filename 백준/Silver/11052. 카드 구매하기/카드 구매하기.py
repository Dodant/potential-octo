n = int(input())
arr = list(map(int, input().split()))

# n = 5
# arr = [1, 9, 18, 25, 1]

dp_arr = [0] * n
dp_arr[0] = arr[0]
dp_arr[1] = max(2*arr[0], arr[1])
# print(dp_arr)
for i in range(2, n):
    for j in range(0, i-1):
        # print(i, j, i-j-1, dp_arr[j], dp_arr[i-j-1])
        dp_arr[i] = max(dp_arr[i], arr[i], dp_arr[j]+dp_arr[i-j-1])
    # print()
print(dp_arr[-1])