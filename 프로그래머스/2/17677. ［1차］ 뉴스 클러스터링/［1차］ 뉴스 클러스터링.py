def solution(str1, str2):
    answer = 0
    str1_ls = [str1[i:i+2].lower() for i in range(len(str1)-1)]
    str2_ls = [str2[i:i+2].lower() for i in range(len(str2)-1)]
    str1_lsc = [i for i in str1_ls if i.isalpha()]
    str2_lsc = [i for i in str2_ls if i.isalpha()]

    a_temp = str1_lsc.copy()
    a_result = str1_lsc.copy()
    
    for i in str2_lsc:
        if i not in a_temp: a_result.append(i)
        else: a_temp.remove(i)
            
    result = []
    for i in str2_lsc:
        if i in str1_lsc:
            str1_lsc.remove(i)
            result.append(i)

    if len(result) == 0 and len(a_result) == 0: answer = 1
    else: answer = len(result) / len(a_result)
    
    return int(answer * 65536)