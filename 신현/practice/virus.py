# https://www.acmicpc.net/problem/2606
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V = int(input())
E = int(input())

graph =  [[] for _ in range(V+1)]
visited = [False] * (V+1)
answer = 0
for _ in range(E):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(v):
    global answer
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            answer+=1
            dfs(i)

dfs(1)
print(answer)        