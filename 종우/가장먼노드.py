# 0328
# https://school.programmers.co.kr/learn/courses/30/lessons/49189


# first attempt
from collections import defaultdict

answer = 0
graph = defaultdict(list)
visited = defaultdict(list)
shortest = []

def solution(n, edge):
    global shortest
    
    for a, b in edge:
        graph[a].append(b)
        visited[a].append(0)
    shortest = [0] * n
    
    stack = graph[1]
    print(graph)
            
    
    return answer

# solution
def solution(n, edge):
    answer = 0
    adj = [[] for i in range(n+1)]
    visited = [0]*(n+1)
    
    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)
    
    queue = [1]
    visited[1] = 1
    
    while queue:
        cur = queue.pop(0)
        
        for node in adj[cur]:
            if not visited[node]:
                visited[node] = visited[cur] +1
                queue.append(node)
    
    return visited.count(max(visited))