from pprint import pprint

def solution(n, results):
    def fw():    
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist

    dist = [[100] * (n+1) for i in range(n+1)]
    for i in range(1, n+1): dist[i][i] = 0
    for a, b in results: dist[a][b] = 1
    dist = fw()
    cnt_arr = [0] * n
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] != 100: cnt_arr[j-1] += 1
            
    for j in range(1, n+1):
        for i in range(1, n+1):
            if dist[i][j] != 100: cnt_arr[i-1] += 1
            
    return cnt_arr.count(n+1)