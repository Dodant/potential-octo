from collections import deque

S = deque(list(input()))

st = deque()
tag_st = deque()
answer = ''

while S:
    c = S.popleft()
    if c == '<':
        while st:
            answer += st.pop()
        tag_st.append(c)
        while S:
            c = S.popleft()
            if c == '>':
                tag_st.append(c)
                break
            else:
                tag_st.append(c)
        while tag_st:
            answer += tag_st.popleft()
    elif c == ' ':
        while st:
            answer += st.pop()
        answer += ' '
    else:
        st.append(c)

while st:
    answer += st.pop()

print(answer)