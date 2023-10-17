from collections import deque

def bfs(board, start_point, end_point, visited):
    q = deque()
    q.append([start_point, 0])
    
    while q:
        point, cnt = q.popleft()
        if point == end_point: return cnt
        else:
            for i in ['U', 'R', 'D', 'L']:
                new_point = move_til_end(board, i, point)
                if visited[new_point[0]][new_point[1]] > cnt + 1:
                    visited[new_point[0]][new_point[1]] = cnt + 1
                    q.append([new_point, cnt+1])
                
    return -1

def move_til_end(board, direction, point):
    result = True
    while result:
        result, point = move(board, direction, point)
    return point
        
def move(board, direction, point):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    di = ['U', 'R', 'D', 'L']
    
    nx = dx[di.index(direction)]
    ny = dy[di.index(direction)]
    
    if point[0] + nx < 0 or point[0] + nx >= len(board) or point[1] + ny < 0 or point[1] + ny >= len(board[0]):
        return False, point
    elif board[point[0] + nx][point[1] + ny] == '.':
        return True, [point[0] + nx, point[1] + ny]
    elif board[point[0] + nx][point[1] + ny] == 'D':
        return False, point
    elif board[point[0] + nx][point[1] + ny] == 'G':
        return True, [point[0] + nx, point[1] + ny]
    elif board[point[0] + nx][point[1] + ny] == 'R':
        return False, point
    
def solution(board):
    start_point = [0, 0]
    end_point = [0, 0]

    visited = [[1000 for _ in range(len(board[0]))] for _ in range(len(board))]
    
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R': 
                start_point = [i, j]
                board[i] = board[i][:j] + '.' + board[i][j+1:]
            if board[i][j] == 'G': 
                end_point = [i, j]
    visited[start_point[0]][start_point[1]] = 0
    answer = bfs(board, start_point, end_point, visited)
    return answer