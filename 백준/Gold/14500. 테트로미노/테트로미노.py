N, M = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(N)]


tetrinos = [
    [[1,1,1,1]],
    [[1],[1],[1],[1]],
    
    [[1,1],
     [1,1]],
    
    [[1,0],
     [1,0],
     [1,1],],
    [[1,1],
     [0,1],
     [0,1],],
    [[1,0],
     [1,1],
     [0,1],],
    [[0,1],
     [1,1],
     [1,0],],
    [[0,1],
     [0,1],
     [1,1],],
    [[1,1],
     [1,0],
     [1,0],],
    [[0,1],
     [1,1],
     [0,1],],
    [[1,0],
     [1,1],
     [1,0],],
    
    [[1,1,1],
     [0,1,0]],
    [[1,1,1],
     [0,0,1]],
    [[1,1,1],
     [1,0,0]],
    [[1,0,0],
     [1,1,1]],
    [[0,0,1],
     [1,1,1]],
    [[0,1,0],
     [1,1,1]],
    [[0,1,1],
     [1,1,0]],
    [[1,1,0],
     [0,1,1]],
]

maxval = []
for tetri in tetrinos:
    h, w = len(tetri), len(tetri[0])
    for i in range(N-h+1):
        for j in range(M-w+1):
            val = 0
            for hh in range(h):
                for ww in range(w):
                    val += tetri[hh][ww] * ls[i+hh][j+ww]

            maxval.append(val)
print(max(maxval))
# print(maxval)    