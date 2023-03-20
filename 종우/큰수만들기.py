# 0320
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

# initial
def solution(number, k):
    nums = [int(i) for i in number]
    for i in range(k):
        nums.remove(min(nums))
        
    return ''.join(str(i) for i in nums)

# next 시간초과
from itertools import combinations

def solution(number, k):
    nums = [int(i) for i in number]
    potential = combinations(nums, len(number) - k)
    potnums = []
    for p in potential:
        tmp = ''.join(str(i) for i in p)
        potnums.append(int(tmp))
        
    return str(max(potnums))

# final

