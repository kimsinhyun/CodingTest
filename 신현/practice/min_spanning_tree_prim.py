# # https://www.acmicpc.net/problem/1197

import sys
input = sys.stdin.readline
import heapq

V, E = map(int,input().split())
visited = [False] * (V+1)
edge_list = [[] for _ in range(V+1)]


for i in range(E):
    start, end, weight = map(int,input().split())
    edge_list[start].append([weight,end])
    edge_list[end].append([weight, start])



def prim(weight, start):
    q = [[weight, start]]
    answer = 0
    cnt = 0
    while cnt < V:
        w, v = heapq.heappop(q)
        if visited[v] == True: 
            continue
        else:
            visited[v] = True
            answer += w
            cnt += 1
            for w, u in edge_list[v]:
                heapq.heappush(q, [w,u])
    return answer   
answer = prim(0,1)
print(answer)