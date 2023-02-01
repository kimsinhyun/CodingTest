# 0201_1
# https://school.programmers.co.kr/learn/courses/30/lessons/42898

# bfs not optimized
def solution(m, n, puddles):    
    return bfs(m, n, puddles)

def bfs(x, y, puddles):
    if x == 0 or y == 0 or [x,y] in puddles:
        return 0
    if x == 1 and y == 1:
        return 1
    
    return bfs(x-1, y, puddles) + bfs(x, y-1, puddles)


# dp but still needs more optimization

def solution(m, n, puddles):
    dp = []
    for i in range(n):
        dp.append([0]*m)
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = -1
    dp[0][0] = 1
    q = [(0,0)]
    visited = [(0,0)]
    
    while q:
        cur = q.pop(0)
        x,y = cur[1], cur[0]
        nx, ny = cur[1]+1, cur[0]+1
        
        if nx < m and dp[y][nx] != -1:
            if (y, nx) not in visited:
                visited.append((y, nx))
                q.append((y,nx))
            dp[y][nx] += dp[y][x]
        if ny < n and dp[ny][x] != -1:
            if (ny, x) not in visited:
                visited.append((ny, x))
                q.append((ny, x))
            dp[ny][x] += dp[y][x]
    
    print(dp)
    return dp[-1][-1]

# 