# 최댓값과 최솟값
# 10.03
# https://school.programme  rs.co.kr/learn/courses/30/lessons/12939?language=python3

def solution(s):
    toarr = [int(x) for x in s.split()]
    answer = str(min(toarr)) + " " + str(max(toarr))
    return answer