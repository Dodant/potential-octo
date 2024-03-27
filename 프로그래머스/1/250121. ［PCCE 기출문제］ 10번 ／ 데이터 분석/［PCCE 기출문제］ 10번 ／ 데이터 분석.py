def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    new_data = []
    ext_idx = ["code", "date", "maximum", "remain"].index(ext)
    for i in data:
        if val_ext >= i[ext_idx]: new_data.append(i)
    idx = ["code", "date", "maximum", "remain"].index(sort_by)
    new_data.sort(key=lambda x:x[idx])
    return new_data