n = int(input())
x, y, z = 0, 0, 0

if n >= 300:
    x = n // 300
    n = n % 300
    
if n >= 60:
    y = n // 60
    n = n % 60
    
if n >= 10:
    z = n // 10
    n = n % 10
    
if n != 0:
    print(-1)
else:    
    print(x,y,z)