import sys
input = sys.stdin.readline
from collections import deque

M, N, D = map(int, input().strip().split(" "))
graph = [[list(map(int,input().strip().split(" "))) for _ in range(N)] for _ in range(D)]
g_queue = deque()

for z in range(D):
    for x in range(N):
        for y in range(M):
            if(graph[z][x][y] == 1):
                # x y z
                g_queue.append((x,y,z))

#x y z
dx_dy_dz =  [1,0,0], [-1,0,0], [0,1,0], [0,-1,0],\
            [0,0,1],[0,0,-1]

def bfs():
    while g_queue:
        x,y,z = g_queue.popleft()
        for dx,dy,dz in dx_dy_dz:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if (0<= nz < D) and (0<= nx < N) and (0<= ny < M):
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    g_queue.append((nx,ny,nz))

bfs()
def day_count():
    day = 0
    for i in graph:
        for j in i:
            for k in j:
                if(k == 0):
                    return -1
        day = max(day,max(j))
    return day
  
day = day_count()
print(day-1)