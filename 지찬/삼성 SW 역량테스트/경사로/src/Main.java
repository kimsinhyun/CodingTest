//https://www.acmicpc.net/problem/14890
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	static int n, l;

	public static boolean check(int[] path) {
		boolean[] ramp = new boolean[n];
		for (int i = 0; i < n - 1; i++) {
			if (path[i] == path[i + 1]) { // 같은 높이
				continue;
			} else if (path[i] < path[i + 1]) { // 올라가야 하는 경
				if (path[i + 1] - path[i] > 1) {
					return false;
				} else {
					if (i - l + 1 < 0)
						return false;
					for (int j = i; j >= i - l + 1; j--) {
						if (path[i] != path[j] || ramp[j] == true)
							return false;
						ramp[j] = true;
					}
				}
			} else { // 내려가야 하는 경우
				if (path[i] - path[i + 1] > 1)
					return false;
				else {
					if (i + l >= n)
						return false;
					for (int j = i + 1; j <= i + l; j++) {
						if (path[i + 1] != path[j] || ramp[j] == true)
							return false;
						ramp[j] = true;
					}
				}
			}
		}
		return true;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		l = Integer.parseInt(st.nextToken());
		int[][] map = new int[n][n];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int[] temp1 = new int[n];
		int[] temp2 = new int[n];
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				temp1[j] = map[i][j];
				temp2[j] = map[j][i];
			}
			if (check(temp1))
				cnt++;
			if (check(temp2))
				cnt++;

		}
		System.out.println(cnt);

	}

}
