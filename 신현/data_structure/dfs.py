import sys
from collections import deque
input = sys.stdin.readline

N, M , V = map(int, input().split())
graph =[[] for _ in range(N+1)]
dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
print(graph) 
def dfs(v):
    dfs_visited[v] = True
    print(v, end=" ")
    for i in range(1, N+1):
        if dfs_visited[i] == False:
            dfs(i)
        
def bfs(v):
    bfs_visited[v] = True
    queue = deque([v])
    while queue:
        n = queue.popleft()
        print(n, end=" ")
        for x in graph[n]:
            if not bfs_visited[x]:
                print("x", x)
                queue.append(x)
                bfs_visited[x] = True
        
               
bfs(V)     
# dfs(V)