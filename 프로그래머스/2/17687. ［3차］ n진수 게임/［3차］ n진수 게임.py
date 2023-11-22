def make_base(n, q):
    base = ''
    if n == 0:
        return '0'
    
    while n > 0:
        n, k = divmod(n, q)
        if k >= 10:
            base += 'ABCDEF'[k-10]
        else:
            base += str(k)
    return base[::-1]


def solution(n, t, m, p):
    answer = ''
    
    for i in range(0, t*m):
        answer += str(make_base(i, n))

    return answer[p-1::m][:t]