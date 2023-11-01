N = int(input())
M = int(input())
S = input()

comp = 'IO' * N + 'I'
cnt = 0
for i in range(0, M-(N*2)):
    if S[i:i+(2*N+1)] == comp: cnt += 1
print(cnt)