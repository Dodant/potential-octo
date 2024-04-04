n, m = map(int, input().split())

garo = 0
sero = 0
map_ = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        map_[i][j] = '0' if map_[i][j] == '.' else '1'
    
for i in range(n):
    if 0 == int(''.join(map_[i])):
        garo += 1

map_ = list(zip(*map_))

for i in range(m):
    if 0 == int(''.join(map_[i])):
        sero += 1
        
print(max(garo, sero))
