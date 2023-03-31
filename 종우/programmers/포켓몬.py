# 0220
# 해시

def solution(nums):
    div2 = len(nums)/2
    types = set()
    for i in nums:
        types.add(i)
    
    return min(len(types), div2)

def solution(nums):
    return min(len(set(nums)), len(nums)/2)