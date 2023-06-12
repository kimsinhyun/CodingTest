# 0612
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque

def solution(maps):
    answer = []
    islands = [[0 if x == "X" else int(x) for x in y] for y in maps]
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)): # i = y
        for j in range(len(maps[0])): # j = x
            if islands[i][j] != 0 and visited[i][j] == 0:
                answer.append(countfood(islands, visited, i, j))
    if answer == []:
        return [-1]
    answer.sort()
    return answer

def countfood(islands, visited, i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    food = 0
    
    q = deque()
    # bfs
    q.append([i,j])
    visited[i][j] = 1
    while q:
        y, x = q.popleft()
        food += islands[y][x]
        for ind in range(4):
            nx = x + dx[ind]
            ny = y + dy[ind]
            if nx >= 0 and ny >= 0 and ny < len(islands) and nx < len(islands[0]):
                if visited[ny][nx] == 0 and islands[ny][nx] != 0:
                    q.append([ny, nx])
                    visited[ny][nx] = 1
    if food == 0:
        return None
    return food
    