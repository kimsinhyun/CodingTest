import sys
from collections import deque
input = sys.stdin.readline

N, M , V = map(int, input().split())
graph =[[0]*(N+1) for _ in range(N+1)]

dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1
    
def dfs(v):
    dfs_visited[v] = True
    print(v, end=" ")
    for i in range(len(graph[v])):
        if(graph[v][i] == 1):
            if dfs_visited[i] == False:
                dfs_visited[i] = True
                dfs(i)
                
def bfs(v):
    bfs_visited[v] = True
    queue = deque([v])
    while queue:
        val = queue.popleft()
        print(val, end=" ")
        for i in range(len(graph[v])):
            if(graph[v][i] == 1):
                if (bfs_visited[i] == False):
                    bfs_visited[i] = True
                    queue.append(i)

dfs(V)
print()
bfs(V)
            