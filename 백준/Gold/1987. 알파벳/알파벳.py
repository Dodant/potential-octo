r, c = map(int, input().split())
board = [list(input()) for i in range(r)]

answer = 1

dx = [0,1,-1,0]
dy = [1,0,0,-1]

def dfs(path, x, y):
    global answer
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in path:
            new_path = path + board[nx][ny]
            answer = max(answer, len(new_path))
            dfs(new_path, nx, ny)
    
x, y = 0, 0
dfs(board[x][y], x, y)
print(answer)