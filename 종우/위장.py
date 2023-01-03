# 0103_2
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

# 내 풀이

def solution(clothes):
    answer = 1
    categorize = {}
    # divide into categories
    for item in clothes:
        if item[1] in categorize:
            categorize[item[1]] += 1
        else:
            categorize[item[1]] = 2

    # get combinations
    for cat in categorize.values():
        answer *= cat
    answer -=1

    return answer

# 다른 풀이

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer