# https://www.acmicpc.net/problem/7562
# input:
# 3
# 8
# 0 0
# 7 0
# 100
# 0 0
# 30 50
# 10
# 1 1
# 1 1

# result
# 5
# 28
# 0

import sys 
from collections import deque
input = sys.stdin.readline

N = int(input())

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

answer = []
def bfs(sx,sy,ex,ey, count, visited):
    queue = deque()
    visited[sx][sy] = True
    queue.append((sx,sy,ex,ey, count))
    while(queue):
        tx, ty, ex, ey, t_count = queue.popleft()
        if((tx == ex) and (ty==ey)):
            # print(f"{t_count}")
            return t_count
        for i in range(len(dx)):
            nx, ny = dx[i]+tx, dy[i]+ty
            if((0<= nx < SIZE) and (0<= ny < SIZE)):
                if(visited[nx][ny] == False):
                    queue.append((nx,ny,ex,ey,t_count+1))
                    visited[nx][ny] = True

for i in range(N):
    SIZE = int(input())
    visited = [[False] * SIZE for _ in range(SIZE)]
    sx,sy = map(int,input().split(" "))
    ex,ey = map(int,input().split(" "))
    answer.append(bfs(sx,sy,ex,ey, 0, visited))

for i in answer:
    print(i)    
    