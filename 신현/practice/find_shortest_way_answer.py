import heapq
from re import L
import sys

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
start_v = int(input())
dq = [INF]*(V+1)
graph = [[] for _ in range(V+1)]
heap = []

for _ in range(E):
    a,b,w = map(int,input().split())
    graph[a].append([w,b])

    
def Dijkstra(v):
    dq[v] = 0
    heapq.heappush(heap, (0,v))
    while heap:
        wei, now = heapq.heappop(heap)
        if dq[now] < wei:
            continue
        for w, next in graph[now]:
            next_wei = w + wei
            if next_wei < dq[next]:
                dq[next] = next_wei
                heapq.heappush(heap, (next_wei, next))
                
Dijkstra(start_v)
for i in range(1, V+1):
    print("INF" if dq[i] == INF else dq[i])