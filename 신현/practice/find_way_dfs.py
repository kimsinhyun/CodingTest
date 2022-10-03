# https://www.acmicpc.net/problem/11403

import sys
input = sys.stdin.readline

n = int(input())
visit = [0 for i in range(n)]
s = []
def dfs(v):
    for i in range(n):
        if visit[i] == 0 and s[v][i] == 1:
            visit[i] = 1
            dfs(i)
for i in range(n):
    s.append(list(map(int, input().split())))
for i in range(n):
    dfs(i)
    print(*visit)
    visit = [0 for i in range(n)]