n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp_0 = 1
    dp_1 = 2
    for i in range(2, n):
        temp = dp_1
        dp_1 = dp_1 + dp_0
        dp_0 = temp
        
        dp_0 = dp_0%15746
        dp_1 = dp_1%15746
    
    print(dp_1)