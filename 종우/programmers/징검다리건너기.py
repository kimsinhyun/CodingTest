# 0525
# https://school.programmers.co.kr/learn/courses/30/lessons/64062

# 효율성 x 
def solution(stones, k):
    answer = 0
    while check(stones, k):
        answer += 1
        subtract(stones)
    return answer

def subtract(stones):
    for i in range(len(stones)):
        stones[i] = stones[i]-1

def check(stones, k):
    skip = 0
    for s in stones:
        if s < 1:
            skip += 1
        else:
            skip = 0
        if skip == k:
            return False
    return True

# sliding window로 k 구간을 확인하고 heap으로 최대값