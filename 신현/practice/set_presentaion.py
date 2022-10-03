# https://www.acmicpc.net/problem/1717

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N, M = map(int, input().split())
parents = [i for i in range(N+1)]

# 작은 쪽에 union
        
def find_parent(a):
    if(parents[a] != a):
        parents[a] = find_parent(parents[a])
        return parents[a]
    return a

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if (a<b):
        parents[b] = a
    else:
        parents[a] = b       

for i in range(M):
    op, a, b = map(int,input().split())
    if op == 0:
        union(a,b)
    else:
        if(find_parent(a) == find_parent(b)):
            print("YES")
        else:
            print("NO")