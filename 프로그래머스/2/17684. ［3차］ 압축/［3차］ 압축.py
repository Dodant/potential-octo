def solution(msg):
    answer = []
    
    dictionary = dict()
    idx = 1
    
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        dictionary[i] = idx
        idx += 1
    
    while msg != '':
        for i in sorted(list(dictionary.keys()), key=lambda x: -len(x)):
            if i == msg[:len(i)]:
                if len(msg) == len(i):
                    answer.append(dictionary[i])
                    msg = ''
                    break
                else:
                    w = i
                    c = msg[len(i)]
                    answer.append(dictionary[i])
                    dictionary[w+c] = idx
                    msg = msg[len(i):]
                    idx += 1
                    break
    return answer