import math

def time_invert(time_str):
    hr, mn = map(int, time_str.split(':'))
    return hr * 60 + mn
    
def solution(fees, records):
    answer = []
    inlist = dict()
    cars = dict()
    for i in records:
        time_, number_, type_ = i.split()
        if type_ == 'IN':
            inlist[number_] = time_invert(time_)
            if number_ not in cars:
                cars[number_] = 0
        elif type_ == 'OUT':
            out_time = time_invert(time_)
            in_time = inlist[number_]
            del inlist[number_]
            if number_ in cars:
                cars[number_] += out_time - in_time
            else:
                cars[number_] = out_time - in_time

    for i in inlist:
        cars[i] += time_invert('23:59') - inlist[i]
            
    carnum = list(cars)
    carnum.sort()

    for i in carnum:
        if cars[i] < fees[0]:
            answer.append(fees[1])
        else:
            price = fees[1]
            price += math.ceil((cars[i] - fees[0] )/ fees[2]) * fees[3]
        
            answer.append(price)
    
    return answer