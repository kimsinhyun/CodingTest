# https://www.acmicpc.net/problem/1197
from gettext import find
import sys 
input = sys.stdin.readline

V, E = map(int,input().split())
parents = [i for i in range(V+1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int,input().split())))
Elist = sorted(Elist, key=lambda x: x[2])

def find_parent(a):
    if(parents[a] == a):
        return a
    else:
        parents[a] = find_parent(parents[a])
        return parents[a]

def union_parent(a,b):
    pa = find_parent(a)
    pb = find_parent(b)
    if(pa == pb):
        return 
    elif (pa < pb):
        parents[pb] = pa
    elif(a > b):
        parents[pa] = pb

answer = 0
temp_num = 0
for start,end,weight in Elist:
        pa = find_parent(start)
        pb = find_parent(end)
        if(pa == pb):
            pass
        else:
            answer += weight
            union_parent(pa, pb)
            temp_num+=1
            
print(answer)        
        