# 1127_1
# https://school.programmers.co.kr/learn/courses/30/lessons/12953

import math

def solution(arr):
    # LCM = L*R/GCF
    LCM = 0
    prev = arr[0]
    for i in range(1, len(arr)):
        cur = arr[i]
        LCM = prev*cur/math.gcd(prev, cur)
        prev = int(LCM)
    return LCM
        

# 그냥 math.gcd 쓰면 돼서 밑에 GCF안씀
# 모듈로 2가 문제이긴 함
def GCF(l, r):
    ans = 1
    if l<r:
        if r%l == 0:
            return l
        for j in range(1, l//2):
            if (l % j == 0) and (r % j ==0):
                ans = j
    else:
        if l%r ==0:
            return r
        for j in range(1, r//2):
            if (l % j == 0) and (r % j ==0):
                ans = j
    return int(ans)
    
# GCF 만든는 바른 방법
def GCF(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd