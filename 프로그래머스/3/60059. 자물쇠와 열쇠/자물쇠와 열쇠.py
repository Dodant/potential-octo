import copy

def rotate(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def check(plat, N, M):
    for i in range(N):
        for j in range(N):
            if plat[M+i-1][M+j-1] != 1:
                return False
    return True

def solution(key, lock):
    M, N = len(key), len(lock)
    plate = [[0] * (N + 2 * M - 2) for _ in range(N + 2 * M - 2)]

    for i in range(N):
        for j in range(N):
            plate[M+i-1][M+j-1] = lock[i][j]

    for i in range(4):
        key = rotate(key)
        for i in range(len(plate) - (M - 1)):
            for j in range(len(plate) - (M - 1)):
                plat = copy.deepcopy(plate)
                flag = False
                for k in range(M):
                    for l in range(M):
                        if plat[i+k][j+l] == 1 and key[k][l] == 1:
                            flag = True
                            break
                        else:
                            plat[i+k][j+l] |= key[k][l]
                    if flag: break

                if check(plat, N, M):
                    return True
    return False