import sys, copy, collections

sys.stdin = open('test1.txt', 'r')
n, m = map(int, sys.stdin.readline().split())
max_num = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
empty_list = []
virus_list = []

EMPTY = 0
WALL = 1
VIRUS = 2

# 입력
g = [[0]*m for _ in range(n)]

for y in range(n):
    raw = [int(x) for x in sys.stdin.readline().split()]

    for x in range(m):
        g[y][x] = raw[x]
        if g[y][x] == EMPTY:
            empty_list.append([y, x])
        if g[y][x] == VIRUS:
            virus_list.append([y, x])

# bfs 탐색
def bfs(ng):
    q = collections.deque([])
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    global max_num

    for virus in virus_list:
        q.append(virus)

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if ng[ny][nx] == EMPTY and visited[ny][nx] == False:
                q.append([ny, nx])
                ng[ny][nx] = VIRUS
                visited[ny][nx] = True
    
    for i in range(n):
        cnt += ng[i].count(EMPTY)
    
    if max_num < cnt:
        max_num = cnt

# 벽 세우기
for i in range(len(empty_list)):
    for j in range(i):
        for k in range(j):
            y1, x1 = empty_list[i]
            y2, x2 = empty_list[j]
            y3, x3 = empty_list[k]

            g[y1][x1] = WALL
            g[y2][x2] = WALL
            g[y3][x3] = WALL

            ng = copy.deepcopy(g)
            bfs(ng)

            g[y1][x1] = EMPTY
            g[y2][x2] = EMPTY
            g[y3][x3] = EMPTY

print(max_num)