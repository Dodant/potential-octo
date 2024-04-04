def solution(phone_book):        
    phone_book_set = set(phone_book)
    phone_book = sorted(phone_book, key=len)
    for i in phone_book_set:
        for j in range(1,21):
            if len(i) <= j: continue
            if i[:j] in phone_book_set: return False
    return True    