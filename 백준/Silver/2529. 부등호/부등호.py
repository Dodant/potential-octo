n = int(input())
arr = list(input().split())
s = []


def dfs(s, direction, n, arr):

    if len(s) == n+1 and check(s, arr):
        return ''.join(map(str, s))
    
    for i in (range(0, 10) if direction == "up" else range(9, -1, -1)):
        if i not in s:
            s.append(i)
            if check(s, arr):
                result = dfs(s, direction, n, arr)
                if result: return result
            s.pop()
            
            
def check(s, arr):
    for i in range(len(s)-1):
        if not eval(f's[i] {arr[i]} s[i+1]'): return False
    return True
       
print(dfs([], 'down', n, arr))
print(dfs([], 'up', n, arr))