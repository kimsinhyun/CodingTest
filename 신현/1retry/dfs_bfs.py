# https://www.acmicpc.net/problem/1260
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

def dfs_recur(v):
    if visited[v] == True:
        return
    else:
        print(v, end=" ")
        visited[v]=True
        for i in range(len(graph[v])):
            dfs_recur(graph[v][i])
            
# def dfs_stack(v):
#     q = deque([v])
#     while q:
#         v = q.pop()
#         visited[v] = True
#         print(v, end=" ")
#         for i in range(len(graph[v])):
#             if(visited[graph[v][i]] == False):
#                 q.append(graph[v][i])
#                 visited[graph[v][i]] = True
def dfs_stack(v):
    q = deque([v])
    while q:
        v = q.pop()
        visited[v] = True
        print(v, end=" ")
        for i in range(len(graph[v])):
            if(visited[graph[v][i]] == False):
                q.append(graph[v][i])
                visited[graph[v][i]] = True
        
def bfs(v):
    queue = deque()
    queue.append(v)

    visited[v] = True

    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for i in graph[current]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                

N,E,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(E):
    start,end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    
for i in range(len(graph)):
    graph[i] = sorted(graph[i])
    print(graph[i])
# dfs_recur(V)
# dfs_stack(V)
bfs(V)