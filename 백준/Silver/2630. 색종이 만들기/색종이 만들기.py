def check(arr):
    return len(set(sum(arr, []))) == 1, arr[0][0]

colors = [0, 0]

def divide(arr):
    n = len(arr)
    result, color = check(arr)
    if result: colors[color] += 1
    else:
        divide([i[:n//2] for i in arr[:n//2]])
        divide([i[n//2:] for i in arr[:n//2]])
        divide([i[:n//2] for i in arr[n//2:]])
        divide([i[n//2:] for i in arr[n//2:]])
    

N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]
divide(ls)
print(colors[0])
print(colors[1])