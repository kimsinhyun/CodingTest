import sys
input = sys.stdin.readline
from collections import deque


M, N = map(int,input().strip().split(" "))
graph = [list(map(int, input().strip().split(" "))) for _ in range(N)]
print(graph)

dx_dy = [[1,0],[-1,0],[0,1],[0,-1]]
g_queue = deque()
for i in range(N):
    for j in range(M):
        if(graph[i][j] == 1):
            g_queue.append((i,j))
print(g_queue)

def bfs():
    while g_queue:
        i, j = g_queue.popleft()
        for x, y in dx_dy:
            nx = i + x
            ny = j + y
            if(0 <= nx < N) and (0<= ny < M):
                if (graph[nx][ny] == 0):
                    graph[nx][ny] = graph[i][j] + 1
                    g_queue.append((nx, ny))
                
bfs()
print(graph)