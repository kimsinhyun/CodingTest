# 0308
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):

    reserve_1 = set(reserve) - set(lost)
    lost_1 = set(lost) - set(reserve)
    reserve_2 = sorted(list(reserve_1), reverse = True)
    lost_2 = sorted(list(lost_1), reverse = True)
    for i in reserve_2:
        if i+1 in lost_2:
            lost_2.remove(i+1)
        elif i-1 in lost_2:
            lost_2.remove(i-1)

    return n - len(lost_2)