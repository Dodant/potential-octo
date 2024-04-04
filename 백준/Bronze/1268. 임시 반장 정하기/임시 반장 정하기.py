n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

answer = []
for i in range(n):
    match_student = set()
    for j in range(5):
        for k in range(n):
            if i == k: continue
            if arr[i][j] == arr[k][j]:
                match_student.add(k)
    answer.append((i+1, len(match_student)))
    
print(sorted(answer, key=lambda x: (x[1], -x[0]))[-1][0])