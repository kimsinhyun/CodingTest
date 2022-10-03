import sys
input = sys.stdin.readline
from collections import deque

T = int(input().strip())
answer = []
for _ in  range(T):
    V, E = map(int,input().split())
    times = [0] + list(map(int,input().split()))
    inDegree = [0]*(V+1)
    graph = [[] for _ in range(V+1)]
    DP = [0] *(V+1)
    for _ in range(E):
        a, b = map(int,input().split())
        graph[a].append(b)
        inDegree[b] += 1
    q = deque()
    for i in range(1, len(inDegree)):
        if inDegree[i] == 0:
            q.append(i)
            DP[i] = times[i]
    while q:
        a = q.popleft()
        for i in graph[a]:
            inDegree[i]-=1
            DP[i] = max(DP[a] + times[i], DP[i])
            if(inDegree[i]==0):
                q.append(i)
    
    answer_idx = int(input().strip())
    answer.append(DP[answer_idx])
    
for i in answer:
    print(i)