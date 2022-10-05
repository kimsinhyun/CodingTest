//https://www.acmicpc.net/problem/13458
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int B, C;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		
		int[] rooms = new int[N];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) {
			rooms[i] = Integer.parseInt(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		B = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		long answer = 0;
		
		for(int i : rooms) {
			int students = i;
			students -= B;	//총감독관 1
			answer++;
			if(students > 0) {	//부감독관
				answer += (students + C - 1) / C;
			}
		}
		
		System.out.println(answer);

	}

}