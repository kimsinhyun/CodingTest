import sys
input = sys.stdin.readline
INF = sys.maxsize
import heapq

V, E = map(int, input().split())
start = int(input())
dq = [INF] * (V+1)
graph = [[] for _ in range(V+1)]
heap = []

for _ in range(E):
    a,b,w = map(int,input().split())
    graph[a].append([w,b])

def Dijkstra(v):
    dq[v] = 0
    heapq.heappush(heap, [0,v])
    while heap:
        now_w, now_v = heapq.heappop(heap)
        if dq[now_v] < now_w:
            continue
        for next_w, next_v in graph[now_v]:
            sum_w = next_w + now_v
            if(sum_w < dq[next_v]):
                dq[next_v] = sum_w
                heapq.heappush(heap, (sum_w, next_v))

Dijkstra(start)
for i in range(1,V+1):
    print("INF" if dq[i]==INF else dq[i])