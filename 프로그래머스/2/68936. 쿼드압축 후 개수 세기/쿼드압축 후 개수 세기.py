def solution(arr):
    zo = [0, 0]
    if len(arr) == 1:
        zo[arr[0][0]] += 1
        return zo
    if len(set(sum(arr, []))) == 1:
        zo[arr[0][0]] += 1
        return zo
    recur(arr, zo)
    return zo

def quad_tree_slice(arr, q):
    arr_ = []
    if q == 1:
        for i in range(len(arr)//2): 
            arr_.append(arr[i][:len(arr)//2])
    if q == 2:
        for i in range(len(arr)//2): 
            arr_.append(arr[i][len(arr)//2:])
    if q == 3:
        for i in range(len(arr)//2, len(arr)): 
            arr_.append(arr[i][:len(arr)//2])
    if q == 4:
        for i in range(len(arr)//2, len(arr)): 
            arr_.append(arr[i][len(arr)//2:])
    return arr_
            
def recur(arr, zo):
    if len(arr) == 1: return
    for i in range(1, 5):
        arr_ = quad_tree_slice(arr, i)
        if len(set(sum(arr_, []))) == 1:
            zo[arr_[0][0]] += 1
        elif len(arr_) == 1:
            zo[arr_[0][0]] += 1
        else:
            recur(arr_, zo)