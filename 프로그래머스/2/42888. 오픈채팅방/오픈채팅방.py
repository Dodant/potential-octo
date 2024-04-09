def solution(record):
    answer = []
    is_map = {}
    for i in record:
        splited_list = i.split()
        if len(splited_list) == 3:
            type_, id_, nickname = splited_list
            if type_ == 'Enter':
                is_map[id_] = nickname
                answer.append(f'is_map["{id_}"]$님이 들어왔습니다.')
            if type_ == 'Change':
                is_map[id_] = nickname
        if len(splited_list) == 2:
            type_, id_ = splited_list
            answer.append(f'is_map["{id_}"]$님이 나갔습니다.')

    new_answer = []
    for i in answer:
        a, b = i.split('$')
        new_answer.append(f'{eval(a)}'+b)
    return new_answer