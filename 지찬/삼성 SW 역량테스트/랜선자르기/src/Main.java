//https://www.acmicpc.net/problem/1654
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		int k, n;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		k = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		int[] lines = new int[k];
		long total = 0;
		for (int i = 0; i < k; i++) {
			int temp = Integer.parseInt(br.readLine());
			lines[i] = temp;
			total += temp;
		}

		long highest = total / n;
		long l = 1, r = highest;
		long mid = (l+r) / 2;

		while (l <= r) {
			long num = 0;
			for (int i = 0; i < k; i++) {
				num += lines[i] / mid;
			}
			if (num < n) {
				r = mid - 1;
				mid = (l + r) / 2;
			} else {
				l = mid + 1;
				mid = (l + r) / 2;
			}
		}

		System.out.println(mid);
	}

}
