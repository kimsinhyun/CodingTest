# 1008_2
# 피보나치 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12945

# 피보나치 iterative solution

bignum = 1234567
def solution(n):
    a,b = 0,1
    for i in range(1, n):
        a, b = b, (a%bignum+b%bignum)%bignum
    return b