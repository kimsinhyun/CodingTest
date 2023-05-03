# 0503
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    combs = []
    
    for order in orders:
        for i in course:
            tosort = list(combinations(order, i))
            for ts in tosort:
                combs.append(tuple(sorted(list(ts))))
    
    potential = Counter(combs)
    counter = [0 for i in range(course[-1])]
    print(potential)
    for poten in potential:
        if len(poten) in course:
            if potential[poten] >= counter[len(poten)-1]:
                print(counter)
                print(poten, potential[poten])
        
    answer.sort()
    
    return answer