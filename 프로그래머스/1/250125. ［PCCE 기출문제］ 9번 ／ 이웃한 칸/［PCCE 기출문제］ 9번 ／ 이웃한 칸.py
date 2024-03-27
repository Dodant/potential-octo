def solution(board, h, w):
    answer = 0
    target = board[h][w]
    upper, left, right, lower = "","","",""
    
    if h != 0:
        upper = board[h-1][w]
        if upper == target: answer += 1
    if w != 0:
        left = board[h][w-1]
        if left == target: answer += 1
    if h != len(board)-1:
        lower = board[h+1][w]
        if lower == target: answer += 1
    if w != len(board[0])-1:
        right = board[h][w+1]
        if right == target: answer += 1
    
    return answer