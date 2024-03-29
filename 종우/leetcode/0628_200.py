# https://leetcode.com/problems/number-of-islands/

from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for i in range(m)]
        islands = 0

        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1" and visited[y][x] == 0:
                    islands += 1
                    q = deque()
                    q.append((x, y))
                    visited[y][x] = 1
                    while q:
                        cx, cy = q.popleft()
                        dx = [-1, 1, 0, 0]
                        dy = [0, 0, -1, 1]
                        for i in range(4):
                            nx, ny = cx+dx[i], cy+dy[i]
                            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                                if grid[ny][nx] == "1" and visited[ny][nx] == 0:
                                    q.append((nx, ny))
                                    visited[ny][nx] = 1
        
        return islands