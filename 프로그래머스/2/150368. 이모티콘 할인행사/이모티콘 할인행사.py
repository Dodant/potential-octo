from itertools import product

def solution(users, emoticons):
    answer = []
    n_emo = len(emoticons)
    rates = [0.9, 0.8, 0.7, 0.6]
    
    def calc(users, emoticons, rates):
        subs = 0
        totp = 0
        for wr, wp in users:
            price = 0
            for emo, rate in zip(emoticons, rates):
                if (100 - wr) / 100 >= rate:
                    price += rate * emo
                if price >= wp:
                    subs += 1
                    break
            else:
                totp += price 
                
        return subs, totp

    for rate in product(*[rates for i in range(n_emo)]):
        answer.append(calc(users, emoticons, rate))
    answer = sorted(answer, key=lambda x: (-x[0], -x[1]))
    return [answer[0][0], int(answer[0][1])]