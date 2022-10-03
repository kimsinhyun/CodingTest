import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    V, E = map(int,input().split())
    times = [0] + list(map(int,input().split()))
    order = [[] for _ in range(V+1)]
    inDegree = [0 for _ in range(V+1)]
    DP = [0 for _ in range(V+1)]

    for i in range(E):
        a,b = map(int, input().split())
        order[a].append(b)
        inDegree[b] += 1
        
    q = deque()
    for i in range(1, V+1):
        if inDegree[i] == 0:
            q.append(i)
            DP[i] = times[i]

    while q:
        a = q.popleft()
        for i in order[a]:
            inDegree[i] -= 1
            DP[i] = max(DP[a] + times[i], DP[i])
            if inDegree[i] == 0:
                q.append(i)
                
    answer = int(input())
    print(DP[answer])