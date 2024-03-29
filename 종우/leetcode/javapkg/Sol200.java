import java.util.*;

// my solution : 9%
class Solution {
    public int numIslands(char[][] grid) {
        int islands = 0;
        int m = grid.length;
        int n = grid[0].length;


        boolean[][] visited = new boolean[m][n];
        Queue<int[]> q = new ArrayDeque<>();

        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    q.offer(new int[] {i, j});
                    islands++;
                    visited[i][j] = true;
                    while (!q.isEmpty()) {
                        int r = q.peek()[0];
                        int c = q.peek()[1];
                        q.poll();
                        for (int k=0; k<4; k++) {
                            int nr = r + dr[k];
                            int nc = c + dc[k]; 
                            if (nr >= 0 && nr < m && nc >= 0 && nc < n 
                                && grid[nr][nc] == '1' && !visited[nr][nc]) {

                                q.offer(new int[] {nr, nc});
                                visited[nr][nc] = true;
                            }
                        }        
                    }
                }
            }
        }
        return islands;
    }
};

class Solution2 {
    int islands = 0;
    int m, n;

    public int numIslands(char[][] grid) {
        m = grid.length;
        n = grid[0].length;

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == '1') {
                    dfs(i, j, grid);
                    islands++;
                }
            }
        }
        return islands;
    }

    private void dfs(int r, int c, char[][] grid) {
        if (r < 0 || c < 0 || r >= m || c >= n || grid[r][c] == '0') return;
        grid[r][c] = '0';

        dfs(r+1, c, grid);
        dfs(r-1, c, grid);
        dfs(r, c+1, grid);
        dfs(r, c-1, grid);
    }
}