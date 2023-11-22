def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    

def solution(n, k):
    answer = 0
    
    base = ''
    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)

    candi = base[::-1].split('0')
    
    for i in candi:
        if i != '' and isprime(int(i)):
            answer += 1
    
    return answer
