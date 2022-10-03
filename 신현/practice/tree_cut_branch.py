# https://www.acmicpc.net/problem/1068
import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N)]
removed = [False] * N
root = None
input_list = list(map(int, input().split(" ")))
answer = 0

for i in range(N):
    if(input_list[i] != -1):
        graph[input_list[i]].append(i)
    else:
        root = i
    
remove_num = int(input())
removed[remove_num] = True

def dfs(v):
    global answer
    if(removed[v] != True):
        if(len(graph[v]) == 0):
            answer += 1
            return
        for i in graph[v]:
            if(removed[i] != True):
                dfs(i)
dfs(root)
print(answer)