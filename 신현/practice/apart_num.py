# https://www.acmicpc.net/problem/2667

import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
graph = []
visited = [[False] * N for _ in range(N)]
# print(visited)
for i in range(N):
    input_str = input().strip()
    graph.append([int(x) for x in input_str])

print("asdasd")
for  i in graph:
    print(i)

dx_dy = [[-1,0],[1,0],[0,-1],[0,1]]
def bfs(x,y):
    print("asd")
    queue = deque([(x,y)])
    count = 0
    while queue:
        x, y = queue.popleft()
        for i,j in (dx_dy):
            nx = x + i
            ny = y + j
            if (0 <= nx < N) and (0 <= ny < N) and (visited[nx][ny]==False) and (graph[nx][ny] == 1):
                count += 1
                visited[nx][ny] = True
                queue.append((nx,ny))
    return count

print(f"graph[0][0] = {graph[0][0]}")
total_counts = []
for i in range(N):
    for j in range(N):
        print(f"graph[{i}][{j}] = {graph[i][j]}")
        if graph[i][j] == 0:
            visited[i][j] = True
        elif graph[i][j] == 1:
            visited[i][j] = True
            total_counts.append(bfs(i,j))

total_counts = sorted(total_counts, reverse=True)
print(total_counts)
            
            