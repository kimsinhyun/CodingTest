# 0122_1
# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    dictionary = {}
    answer = []
    longest = 1
    tmp = ""
    for ch in msg:
        if len(tmp) < longest:
            tmp += ch
            continue
        for i in range(longest):
            lk = tmp[:longest-i]
            print(lk)
                
    return answer