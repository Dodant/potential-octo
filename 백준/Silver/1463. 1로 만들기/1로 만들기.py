N = int(input())
ls = [0, 0] + [100] * (N-1)

for i in range(2, N+1):
    temp = 0
    if i % 3 == 0 and i % 2 == 0:
        ls[i] = min(ls[i//3], ls[i//2], ls[i-1]) + 1
    elif i % 3 == 0:
        ls[i] = min(ls[i//3], ls[i-1]) + 1
    elif i % 2 == 0:
        ls[i] = min(ls[i//2], ls[i-1]) + 1
    else:
        ls[i] = ls[i-1] + 1

print(ls[-1])