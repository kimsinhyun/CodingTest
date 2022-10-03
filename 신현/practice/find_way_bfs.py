# https://www.acmicpc.net/problem/11403

from re import L
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
def bfs(start):
    dq = deque([start])
    while dq:
        v = dq.popleft()
        for j in range(N):
            if(visited[j] == 0) and (graph[v][j]==1):
                visited[j] = 1
                dq.append(j)

for i in range(N):
    visited = [0] * (N)
    bfs(i)
    print(*visited)
    visited = [0] * (N)
    
