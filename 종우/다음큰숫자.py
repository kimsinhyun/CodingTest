# 1008_3
# 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    bincount = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == bincount:
            break
    return n