# 0325
# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    answer = ["ICN"]
    flights = {}
    
    # start in ICN
    # stores flights in hashmap
    for t in tickets:
        if t[0] not in flights:
            flights[t[0]] = []
        flights[t[0]].append(t[1])
    
    for f in flights:
        flights[f].sort()
    
    found = False
    
    answer = dfs(flights, len(tickets), answer)
    
    return answer

def dfs(flights, n, path):
    if len(path) == n:
        return path
    
    cur = path[-1]
    if len(flights[cur]) != 0:
        nx = flights[cur].pop(0)
        path.append(nx)
        dfs(flights, n, path)
        
# dfs solution
import collections
answer = []
graph = collections.defaultdict(list)
visited = collections.defaultdict(list)

def solution(tickets):
    for a,b in tickets:
        graph[a].append(b)
        visited[a].append(0)
    for a,b in graph.items():
        graph[a].sort()
    
    dfs('ICN', ['ICN'], 0, len(tickets))
    
    return answer

def dfs(cur, path, cnt, k):
    if cnt == k:
        global answer
        answer = path
        return
    
    if len(answer) >= 1:
        return
    
    for i in range(len(graph[cur])):
        if not visited[cur][i]:
            visited[cur][i] = 1
            dfs(graph[cur][i], path + [graph[cur][i]], cnt+1, k)
            visited[cur][i] = 0
        