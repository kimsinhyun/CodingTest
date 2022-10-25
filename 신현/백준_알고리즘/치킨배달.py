# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations
def distance(p1,p2): 
    x1,y1=p1 ; x2,y2=p2
    return abs(x1-x2) + abs(y1-y2)

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
homes = []
chickens = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            homes.append([i,j])
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickens.append([i,j])

combs = list(combinations(chickens, m))
answer = []
for cs in combs:
    temp = []
    for h in homes:
        ans = sys.maxsize
        for c in cs:
            ans = min(ans, distance(h,c))
        temp.append(ans)
    answer.append(sum(temp))
print(min(answer))
        
            