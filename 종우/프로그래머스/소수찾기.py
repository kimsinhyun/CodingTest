# 0207
# https://school.programmers.co.kr/learn/courses/30/lessons/42839#

import itertools
import math

def solution(numbers):
    primes = set()
    for i in range(len(numbers)):
        p = itertools.permutations(numbers, i+1)
        for j in p:
            num = int("".join(j))
            if isprime(num):
                primes.add(num)
    return len(primes)

def isprime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True