# https://www.acmicpc.net/problem/11403

from dis import dis
import sys
input = sys.stdin.readline
N = int(input())
distance = [[0]*(N) for _ in range(N)]
graph = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N): 
            if(graph[i][j] == 1) or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1                
for i in graph:
    print(*i)