from collections import deque

def solution(number, k):
    st = deque()
    leng = len(number)
    st.append(number[0])
    number = number[1:]
    
    while True:
        if k == 0: break
        if len(number) != 0:
            if st and st[-1] < number[0]:
                st.pop()
                k -= 1
            else:
                st.append(number[0])
                number = number[1:]
        else:
            return ''.join(list(st)[:leng-k])

    return ''.join(list(st)) + number