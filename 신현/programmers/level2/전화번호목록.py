def solution(phone_book):
    from collections import deque
    answer = True
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        if(phone_book[i+1].startswith(phone_book[i])):
            return False
    # print(phone_book)
    return True
    return answer