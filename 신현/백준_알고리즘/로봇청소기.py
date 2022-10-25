# https://www.acmicpc.net/problem/14503
from collections import deque
n,m = map(int, input().split())
x,y,d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = deque([-1,0,1,0])
dy = deque([0,1,0,-1])
answer = 0
def bfs(x,y,d):
    q = deque([(x,y,d)])
    graph[x][y] = 2
    dx.rotate(-d) ; dy.rotate(-d)
    global answer
    answer+=1
    while q:
        back = True
        x,y,d = q.pop()
        for i in range(len(dx)):
            dx.rotate(1) ; dy.rotate(1)
            nx, ny = x+dx[0], y+dy[0]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny]=2
                q.append((nx,ny,i-1))
                answer+=1
                back=False
                break
        if back and graph[x-dx[0]][y-dy[0]] != 1:
            x = x-dx[0]
            y = y-dy[0]
            q.append((x,y,1))

bfs(x,y,d)
print(answer)