//https://www.acmicpc.net/problem/14499
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N, M, x, y, K;
	
	static int top = 0, bottom = 0, left = 0, right = 0, front = 0, back = 0;
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		x = Integer.parseInt(st.nextToken());
		y = Integer.parseInt(st.nextToken());
		
		K = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[N][M];
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		st = new StringTokenizer(br.readLine());
		
		int[] moves = new int[K];
		for(int i = 0; i < K; i++) {
			moves[i] = Integer.parseInt(st.nextToken());
		}
		
		for(int i = 0; i < K; i++) {
			roll(moves[i], map);
		}
		
	}
	
	static void roll(int move, int[][] map) {
		if(move == 1) {
			if(y + 1 >= M) return;
			else {
				y++;
				int temp = top;
				top = left;
				left = bottom;
				bottom = right;
				right = temp;
				if(map[x][y] == 0) {
					map[x][y] = bottom;
				}
				else {
					bottom = map[x][y];
					map[x][y] = 0;
				}
				System.out.println(top);
				return;
			}
		}
		else if(move == 2) {
			if(y - 1 < 0) return;
			else {
				y--;
				int temp = top;
				top = right;
				right = bottom;
				bottom = left;
				left = temp;
				if(map[x][y] == 0) {
					map[x][y] = bottom;
				}
				else {
					bottom = map[x][y];
					map[x][y] = 0;
				}
				System.out.println(top);
				return;
			}
		}
		else if(move == 3) {
			if(x - 1 < 0) return;
			else {
				x--;
				int temp = top;
				top = front;
				front = bottom;
				bottom = back;
				back = temp;
				if(map[x][y] == 0) {
					map[x][y] = bottom;
				}
				else {
					bottom = map[x][y];
					map[x][y] = 0;
				}
				System.out.println(top);
				return;
			}
		}
		else if(move == 4) {
			if(x + 1 >= N) return;
			else {
				x++;
				int temp = top;
				top = back;
				back = bottom;
				bottom = front;
				front = temp;
				if(map[x][y] == 0) {
					map[x][y] = bottom;
				}
				else {
					bottom = map[x][y];
					map[x][y] = 0;
				}
				System.out.println(top);
				return;
			}
		}
		return;
	}

}
