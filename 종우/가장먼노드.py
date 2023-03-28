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
