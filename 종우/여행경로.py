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
        
        