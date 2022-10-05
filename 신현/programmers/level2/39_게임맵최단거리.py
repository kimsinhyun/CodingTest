def bfs(route,maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    from collections import deque
    q = deque([[0,0]])
    while q:
        v_i,v_j = q.popleft()
        visited[v_i][v_j] = True
        for i,j in route:
            n_i = v_i+i
            n_j = v_j+j
            if  (0<=n_j<len(maps[0]))\
                and (0<=n_i<len(maps))\
                and (maps[n_i][n_j]==1\
                and not visited[n_i][v_j+j]):
                visited[n_i][n_j] = True
                maps[n_i][n_j] = maps[v_i][v_j] + 1
                q.append([n_i,n_j])
            
def solution(maps):
    route = [[1,0],[-1,0],[0,1],[0,-1]]
    print(route)
    bfs(route, maps)
    return maps[len(maps)-1][len(maps[0])-1] if maps[len(maps)-1][len(maps[0])-1]!=1 else -1