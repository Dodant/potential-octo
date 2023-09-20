n = int(input())
x, y = 100, 100

for i in range(n):
    n, m = map(int, input().split())
    if n > m:
        y -= n
    elif n < m:
        x -= m

print(x)
print(y)