import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int minDiff = Integer.MAX_VALUE;
	static int n;
	static boolean[] visited;
	static int[][] map;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		map = new int[n][n];
		
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		visited = new boolean[n];
		combi(0, 0);
		System.out.println(minDiff);
	}
	
	public static void combi(int idx, int cnt) {
		if (cnt == n / 2) {
			diff();
			return;
		}
		for (int i = idx; i < n; i++) {
			if (!visited[i]) {
				visited[i] = true;
				combi(i + 1, cnt + 1);
				visited[i] = false;
			}
		}
	}
	
	public static void diff() {
		int start = 0;
		int link = 0;
		for (int i = 0; i < n - 1; i++) {
			for (int j = i + 1; j < n; j++) {
				if (visited[i] && visited[j]) {
					start += map[i][j];
					start += map[j][i];
				} else if (!visited[i] && !visited[j]) {
					link += map[i][j];
					link += map[j][i];
				}
			}
		}
		int diff = Math.abs(start - link);
		minDiff = Math.min(diff, minDiff);
	}



}