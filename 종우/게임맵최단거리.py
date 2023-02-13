# 0211
# https://school.programmers.co.kr/learn/courses/30/lessons/1844


# my attempt at bfs 효율성x
def solution(maps):
    answer = 0
    x_a = len(maps[0]); y_a = len(maps)
    been = set()
    queue = []
    been.add((0,0))
    queue.append((0,0,1, been))
    
    while queue:
        x, y, l, track = queue.pop(0)
        if x == x_a-1 and y == y_a-1:
            return l
        
        if x < x_a-1 and maps[y][x+1] == 1 and (x+1,y) not in track:
            track1 = track.copy()
            track1.add((x+1,y))
            queue.append((x+1, y, l+1, track1))
        if y < y_a-1 and maps[y+1][x] == 1 and (x,y+1) not in track:
            track2 = track.copy()
            track2.add((x,y+1))
            queue.append((x, y+1, l+1, track2))
        if y > 0 and maps[y-1][x] == 1 and (x,y-1) not in track:
            track3 = track.copy()
            track3.add((x,y-1))
            queue.append((x, y-1, l+1, track3))
        if x > 0 and maps[y][x-1] == 1 and (x-1,y) not in track:
            track4 = track.copy()
            track4.add((x-1,y))
            queue.append((x-1, y, l+1, track4))
            
    return -1

# cleaner bfs
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = [(0,0)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    visited[0][0] = 1
    distance = {(0,0):1}
    
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]:
                if nx == n-1 and ny == m-1:
                    return distance[(x,y)]+1
                queue.append((nx, ny))
                distance[(nx,ny)] = distance[(x,y)]+1
                visited[nx][ny] = 1
    return -1