//https://www.acmicpc.net/problem/14503
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    static int[] dr = {
            -1, 0, 1, 0
    };
    static int[] dc = {
            0, 1, 0, -1
    };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        int[][] map = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int cnt = 0;
        int cleaned = 1;
        int[][] cleanMap = new int[n][m];
        cleanMap[r][c] = 1;
        while (true) {
            cnt++;
            if (cnt == 5) {
                if (map[r + dr[(d + 2) % 4]][c + dc[(d + 2) % 4]] == 0) {
                    r += dr[(d + 2) % 4];
                    c += dc[(d + 2) % 4];
                    cnt = 0;
                    continue;
                } else {
                    break;
                }
            }
            d = (d + 3) % 4;
            if (cleanMap[r + dr[d]][c + dc[d]] == 0 && map[r + dr[d]][c + dc[d]] == 0) {
                r += dr[d];
                c += dc[d];
                cnt = 0;
                cleanMap[r][c] = 1;
                cleaned++;
            }
        }

        System.out.println(cleaned);
    }
}