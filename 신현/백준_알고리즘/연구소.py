# https://www.acmicpc.net/submit/14502
from copy import deepcopy
from collections import deque
from itertools import combinations
n,m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for i,j in zip(dx,dy):
            nx, ny = x+i, y+j
            if  0<=nx<n and 0<=ny<m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx,ny))

# 0인 index들 모두 추출
z_idxs = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 0:
            z_idxs.append([i,j])
combs = list(combinations(z_idxs,3))

answer = 0
for idxs in combs:
    temp = deepcopy(graph)
    for x,y in idxs:
        temp[x][y] = 1
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if temp[i][j] == 2:
                bfs(i,j)
    ans = 0
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if temp[i][j] == 0:
                ans+=1
    answer = max(answer , ans)
print(answer)