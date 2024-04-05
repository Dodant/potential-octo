from collections import deque

def solution(number, k):
    st = deque()
    number = deque(list(number))
    st.append(number[0])
    number.popleft()
    
    while True:
        if st and st[-1] < number[0]:
            st.pop()
            k -= 1
        else:
            st.append(number[0])
            number.popleft()
            
        if k == 0: 
            return ''.join(list(st)) + ''.join(list(number))
        elif len(number) == 0: 
            return ''.join(list(st)[:-k])

if __name__ == "__main__":
    n, k = map(int, input().split())
    number = input()
    print(solution(number, k))