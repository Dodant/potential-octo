n = int(input())
arr = [int(input()) for i in range(n)]

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
elif n == 3:
    print(max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2]))
else:
    dp = [arr[0], arr[0] + arr[1], max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])]
    for i in range(3, n):
        dp.append(max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1]))
    print(max(dp))
    