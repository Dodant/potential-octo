n, m = map(int, input().split())

def rev(num):
    return int(str(num)[::-1])

print(rev(rev(n) + rev(m)))