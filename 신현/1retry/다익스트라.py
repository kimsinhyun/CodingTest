# 모든 정점간의 최소 거리를 구하는 알고리즘 extra) 다익스트라의 경우 한개의 정점에서 다른 모든 정점의 최단거리를 찾음

import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())
dp = [INF] * (V+1)
graph = [[] for _ in range(V+1)]
heap = []

for i in range(E):
    a,b,w = map(int,input().split())
    graph[a].append((w,b))
    
    
def Dijkstra(v):
    heapq.heappush(heap, (0, v))
    dp[v] = 0
    while heap:
        now_w, now_v = heapq.heappop(heap)
        if dp[now_v] < now_w:
            continue
        for next_w, next_v in graph[now_v]:
            sum_w = next_w + now_w
            print(f"now_v={now_v} ; next_v={next_v} ; sum_w={sum_w} ;dp={dp}")
            if sum_w < dp[next_v]:
                dp[next_v] = sum_w
                heapq.heappush(heap,(sum_w, next_v))
                
Dijkstra(start)
for i in range(1, V+1):
    print("INF" if dp[i]==INF else dp[i])