# 0209
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

# itertools product 중복 순열
from itertools import product
def solution(word):
    answer = 0
    words = []
    for i in range(1, 6):
        c = product(['A','E','I','O','U'], repeat=i)
        for comb in c:
            words.append(''.join(comb))
    words.sort()
    answer = words.index(word) +1
    return answer