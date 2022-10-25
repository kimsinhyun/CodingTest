# https://www.acmicpc.net/problem/10773

from collections import deque
n = int(input())
answer = deque()
for i in range(n):
    temp = int(input())
    if temp == 0:
        answer.pop()
    else:
        answer.append(temp)
print(sum(answer))
