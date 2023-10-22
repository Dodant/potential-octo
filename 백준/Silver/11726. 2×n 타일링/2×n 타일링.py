n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    fibo = [0] * n
    fibo[0] = 1
    fibo[1] = 2

    for i in range(2, n):
        fibo[i] = fibo[i-1] + fibo[i-2]

    print(fibo[-1]%10007)