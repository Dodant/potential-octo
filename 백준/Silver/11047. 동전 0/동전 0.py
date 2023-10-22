N, K = map(int, input().split())
ls = [int(input()) for _ in range(N)]
ls.reverse()
answer = 0

for i in range(N):
    answer += K // ls[i]
    K %= ls[i]

print(answer)