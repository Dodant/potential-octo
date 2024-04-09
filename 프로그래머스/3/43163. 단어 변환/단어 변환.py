from collections import deque

def solution(begin, target, words):
    if target not in words: return 0
    if begin in words: return 1
    q = deque([begin])
    letter_n = len(begin)

    visited = {}
    visited[begin] = True
    for i in words: visited[i] = False
    dist = {}
    dist[begin] = 0
    dist[target] = 0

    while q:
        comp_word = q.popleft()
        for idx in range(letter_n):
            for word in words:
                if visited[word]: continue
                if comp_word[:idx] + comp_word[idx+1:] == word[:idx] + word[idx+1:]:
                    q.append(word)
                    dist[word] = dist[comp_word] + 1
                    visited[word] = True
    
    
    return dist[target]