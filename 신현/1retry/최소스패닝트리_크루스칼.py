# 최소 비용으로 모든 간선을 싸이클 없이 잇는 알고리즘
# https://www.acmicpc.net/problem/1197
import sys
input = sys.stdin.readline

V = int(input())
E = int(input())
parent = [i for i in range(V+1)]
graph = [list(map(int, input().split())) for _ in range(E)]
graph = sorted(graph, key=lambda x: x[2])
print(parent)
print(graph)
def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
        return parent[a]
    return a

def uion(a,b):
    pa,pb = find_parent(a), find_parent(b)
    if pa == pb:
        return
    elif pa < pb:
        parent[pb] = pa 
    else:
        parent[pa] = pb
        
answer = 0
for a,b,w in graph:
    pa, pb = find_parent(a), find_parent(b)      
    if pa == pb:
        pass
    else:
        uion(pa,pb)
        answer += w

print(answer)