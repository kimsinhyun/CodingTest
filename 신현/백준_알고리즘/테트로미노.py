# https://www.acmicpc.net/problem/14500
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
max_graph = max(map(max,graph))
dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = 0
def dfs(x,y,step, total):
    global answer
    if total + max_graph*(4-step) <= answer:
        return
    # for i in range(len(visited)):
    #     for j in range(len(visited[0])):
    #         print("T", end=" ") if visited[i][j] else print("_", end=" ")
    #     print()
    # print()
    if step == 4:
        answer = max(answer, total)
        return
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False:
            if step == 2:
                visited[nx][ny] = True
                dfs(x,y,step+1, total+graph[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx,ny,step+1, total+graph[nx][ny])
            visited[nx][ny] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,graph[i][j])
        visited[i][j] = False
print(answer)
        