# def find_num(c,combs):
#     ttt = len(list(filter(lambda y: "".join(sorted(y)).find(c)!=-1, combs)))
#     return ttt
    
# def solution(orders, course):
#     from itertools import combinations
#     combs = []
#     for o in orders:
#         for num in course:
#             test = list(combinations(list(o),num))
#             test = ["".join(sorted(x)) for x in test]
#             combs.extend(test)
            
#     cdict = dict()
#     for c in combs:
#         if c not in cdict:
#             cdict[c] = 1
#         else:
#             cdict[c] += 1
#     test = sorted(cdict.items(), key=lambda x:x[1],reverse=True)
    
#     most_course = dict()
#     for c in course:
#         most_course[c] = 2
#     answer = []
#     for t in test:
#         if t[1] > most_course[len(t[0])]:
#             most_course[len(t[0])] = t[1]
#             answer.append(t[0])
#         elif t[1] == most_course[len(t[0])]:
#             answer.append(t[0])
#     answer.sort()
#     return answer


def solution(orders, course):
    from itertools import combinations
    from collections import Counter
    combs = []
    for c in course:
        for o in orders:
            combs.extend(list(combinations(o,c)))
    combs = ["".join(sorted(x)) for x in combs]
    counter = Counter(combs)
    # print(counter)
    counter = counter.most_common()
    # print(counter)
    max_dict = dict()
    for c in course:
        max_dict[c] = 2
    answer = []
    for c in counter:
        if c[1] > max_dict[len(c[0])]:
            max_dict[len(c[0])] = c[1]
            answer.append(c[0])
        elif c[1] == max_dict[len(c[0])]:
            answer.append(c[0])
    return sorted(answer)            
