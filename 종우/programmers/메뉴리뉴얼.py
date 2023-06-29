# 0503
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter

from itertools import combinations

def solution(orders, course):
    answer = []
    potential_course = [{} for i in range(len(course))]
    
    for order in orders:
        for i, n in enumerate(course):
            combs = combinations(order, n)
            for c in combs:
                tmp = "".join(sorted(list(c)))
                if tmp not in potential_course[i]:
                    potential_course[i][tmp] = 0
                potential_course[i][tmp] += 1
    
    for i in range(len(course)):
        sorted_pc = sorted(potential_course[i].items(), key=lambda x:x[1], reverse=True)
        if sorted_pc:
            mx = sorted_pc[0][1]
            for pc in sorted_pc:
                if pc[1] == mx and pc[1] >= 2:
                    answer.append(pc[0])
                else:
                    break
    
    return sorted(answer)

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