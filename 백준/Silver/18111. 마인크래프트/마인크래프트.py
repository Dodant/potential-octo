N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

max_height = max(map(max, land))
min_height = min(map(min, land))

time_answer = 1000000000
high_answer = 1000000000

def makeheight(land, N, M, height, inventory, time_answer):
    time = 0
    for i in range(N):
        for j in range(M):
            if land[i][j] < height:
                time += height - land[i][j]
                inventory -= height - land[i][j]
            elif land[i][j] > height:
                time += 2 * (land[i][j] - height)
                inventory += land[i][j] - height
            if time > time_answer:
                return False, 1000000000
    if inventory < 0:
        return False, 1000000000
    return True, time

for i in range(min_height, max_height+1):
    inventory = B
    tf, time = makeheight(land, N, M, i, inventory, time_answer)
    if tf:
        if time < time_answer:
            time_answer = time
            high_answer = i
        elif time == time_answer:
            if i > high_answer:
                high_answer = i
                
print(time_answer, high_answer)
