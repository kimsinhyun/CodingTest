# https://www.acmicpc.net/problem/1967
from dis import dis
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
distance = [-1] * (N+1)
for i in range(1, N):
    parent, child, weight = list(map(int, input().split(" ")))
    graph[parent].append({"child" : child, "weight": weight})
    graph[child].append({"child" : parent, "weight": weight})

def dfs(v, wei):
    # print(f"v = {v}")
    for i in graph[v]:
        next_v = i['child']
        temp_w = i['weight']
        if(distance[next_v] == -1):
            distance[next_v] = temp_w + wei
            dfs(next_v, wei + temp_w)
        
# 가장 먼 leaf node부터 탐색
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드로부터 시작
start = distance.index(max(distance))
distance = [-1] * (N+1)    
distance[start] = 0
dfs(start, 0)
print(max(distance))