# https://www.acmicpc.net/problem/1922
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

parents = [i for i in range(N+1)]
Elist = []
for i in range(M):
    Elist.append(list(map(int, input().split())))
Elist = sorted(Elist, key=lambda x: x[2])

def find_parent(a):
    if parents[a] != a:
        parents[a] = find_parent(parents[a])
        return parents[a]
    return a
    
def union_parent(a,b):
    pa = find_parent(a)
    pb = find_parent(b)
    if pa == pb:
        return 
    elif pa < pb:
        parents[pb] = pa
    else:
        parents[pa] = pb

answer = 0
for a,b,w in Elist:
    pa = find_parent(a)
    pb = find_parent(b)
    if pa == pb:
        continue
    else:
        answer += w
        union_parent(a,b)

print(answer)