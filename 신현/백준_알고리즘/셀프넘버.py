# https://www.acmicpc.net/problem/4673

import sys
input = sys.stdin.readline

def not_self_num(num):
    result = num
    num=str(num)
    for n in num:
        result += int(n)
    return result

not_list = set()
for i in range(1,10000):
    not_list.add(not_self_num(i))
temp = set([i for i in range(1,10000)])

test = list(temp - not_list)
test.sort()
for t in test:
    print(t)