# 0122_1
# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    dictionary = {}
    answer = []
    longest = 1
    trk = 27
    tmp = ""
    for j, ch in enumerate(msg):
        if len(tmp) < longest:
            tmp += ch
            continue
        for i in range(longest):
            lk = tmp[:longest-i]
            if len(lk) == 1:
                answer.append(ord('A')-64)
                tmp = ""
                trk += 1
            elif lk in dictionary:
                answer.append(dictionary[lk])
                tmp = tmp[longest-i:]
                
    return answer