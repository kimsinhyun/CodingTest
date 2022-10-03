# https://www.acmicpc.net/problem/7576
from lib2to3.pgen2 import grammar
import sys
from collections import deque
imput = sys.stdin.readline
M, N = map(int,input().split(" "))

box = [ list(map(int,input().split(" "))) for _ in range(N) ]
print(box)

dx_dy = [[1,0],[-1,0],[0,1],[0,-1]]

queue = deque([])
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i,j))

print(queue)
def bfs():
    while queue:
        i, j = queue.popleft()
        for x, y in dx_dy:
            nx = i + x
            ny = j + y
            if 0 <= nx < N and 0 <= ny < M:
                if(box[nx][ny] == 0):
                    box[nx][ny] = box[i][j] + 1
                    queue.append((nx,ny))
bfs()
for i in box:
    print(i)
def get_days():
    day = 0
    for i in box:
        for j in i:
            if j == 0:
                return -1
        day = max(day, max(i))
    return day
    
print(get_days()-1)
