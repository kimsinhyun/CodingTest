# https://www.acmicpc.net/problem/1922

import sys 
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())
Vlist = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a,b,weight = map(int,input().split())
    Vlist[a].append([weight, b])
    Vlist[b].append([weight, a])
    

def prim(weight, start):
    q = [[weight,start]]
    answer = 0
    cnt = 0
    while cnt < N:
        w, v = heapq.heappop(q)
        if visited[v] == True:
            continue
        else:
            visited[v] = True
            answer+=w
            cnt += 1
            for w,e in Vlist[v]:
                heapq.heappush(q, [w,e])
    return answer    
answer = prim(0,1)
print(answer)