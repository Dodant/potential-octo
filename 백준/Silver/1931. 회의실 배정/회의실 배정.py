N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]

end_ls = sorted(ls, key=lambda x: (x[1], x[0]))
cnt = 1
end_time = end_ls[0][1]
for k in range(1, N):
    if end_time <= end_ls[k][0]:
        cnt += 1
        end_time = end_ls[k][1]

print(cnt)
        