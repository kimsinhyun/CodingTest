# https://www.acmicpc.net/problemset?sort=ac_desc&algo=102

from collections import deque
n,m = map(int,input().split())
temp = deque([i for i in range(1,n+1)])

answer=[]
while temp:
    temp.rotate(-m+1)
    answer.append(temp.popleft())
print("<",end="")
for i in range(len(answer)-1):
    print(answer[i] , end=", ")
print(answer[-1], end="")
print(">")