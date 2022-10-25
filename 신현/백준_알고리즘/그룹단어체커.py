# https://www.acmicpc.net/problem/1316

import sys
input = sys.stdin.readline

def check(str):
    from collections import Counter
    # print(dir(Counter))
    counts = Counter(str)
    for word, cnt in counts.items():
        if str[str.index(word):str.index(word)+cnt].count(word) != cnt:
            return False
    return True
             
n = int(input())
inputs = []
for i in range(n):
    inputs.append(input().strip())

answer = []
for i in inputs:
    answer.append(check(i))
    
print(sum(answer))
