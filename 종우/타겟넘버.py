# 0118_1
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0
    sums = [numbers[0], -numbers[0]]
    numbers.pop(0)
    for i in numbers:
        tmp = []
        for j in sums:
            tmp.append(j+i)
            tmp.append(j-i)
        sums = tmp
    return tmp.count(target)