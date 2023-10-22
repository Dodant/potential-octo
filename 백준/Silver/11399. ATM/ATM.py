N = int(input())
ls = list(map(int, input().split()))
ls.sort()
answer = 0

for i in range(N):
    answer += sum(ls[:i+1])
    
print(answer)