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

# 정답
def solution_itertools(orders, course):
        import itertools

        answer = []

        for size_of_course in course:
            order_dict = {}
            order_combinations = []
            for order in orders:
                order_combinations.extend(list(itertools.combinations(sorted(order), size_of_course)))

            for order_combination in order_combinations:
                order_str = ''.join(order_combination)
                if order_str in order_dict:
                    order_dict[order_str] += 1
                else:
                    order_dict[order_str] = 1

            for order in order_dict:
                if order_dict[order] == max([order_dict[order] for order in order_dict]):
                    if order_dict[order] > 1:
                        answer.append(order)


        return sorted(answer)