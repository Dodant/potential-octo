def solution(want, number, discount):
    answer = 0
    want_list = {}
    for w, n in zip(want, number):
        want_list[w] = n
    
    window = {}
    for i in range(10):
        if discount[i] not in window : window[discount[i]] = 1
        else: window[discount[i]] += 1
        
    if window == want_list: 
        answer += 1
    
    for i in range(len(discount)-10):

        window[discount[i]] -= 1
        if window[discount[i]] == 0: del window[discount[i]]
        if discount[i+10] not in window: window[discount[i+10]] = 1
        else: window[discount[i+10]] += 1
        
        if window == want_list: 
            answer += 1


    
    return answer