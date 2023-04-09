# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
# 0409

import sys
import itertools

sys.stdin = open('test1.txt', 'r')
n = int(input())
nums = list(map(int, input().split(' ')))
operators = list(map(int, input().split(' ')))

print(n, nums, operators)

op = []

for i in range(len(operators)):
    for j in range(operators[i]):
        op.append(i)

opcomb = itertools.permutations(op)
floor = 100000001
ceil = -100000001

for o in opcomb:
    res = nums[0]
    for i in range(n-1):
        if o[i] == 0:
            res = res + nums[i+1]
        elif o[i] == 1:
            res = res - nums[i+1]
        elif o[i] == 2:
            res = res * nums[i+1]
        elif o[i] == 3:
            if res < 0 and nums[i+1] > 0: 
                res = -1*( res*(-1) // nums[i+1])
            res = int(res / nums[i+1])
    ceil = max(ceil, res)
    floor = min(floor, res)

print(ceil)
print(floor)


