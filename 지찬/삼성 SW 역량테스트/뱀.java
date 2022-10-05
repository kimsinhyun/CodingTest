//https://www.acmicpc.net/problem/3190
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static int K;
	static int L;
	
	static LinkedList<Apple> apples = new LinkedList<>();
	static Queue<Move> moves = new LinkedList<>();
	
	static int[] dx = {0, -1, 0, 1}; //세로
	static int[] dy= {1, 0, -1, 0}; //가로

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		K = Integer.parseInt(st.nextToken());
		
		for(int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine());
			apples.add(new Apple(new Position(Integer.parseInt(st.nextToken()) - 1, 
					Integer.parseInt(st.nextToken()) - 1)));
		}
		
		st = new StringTokenizer(br.readLine());
		
		L = Integer.parseInt(st.nextToken());
		
		for(int i = 0; i < L; i++) {	// right = 0, up = 1, left = 2, down = 3
			st = new StringTokenizer(br.readLine());
			moves.add(new Move(Integer.parseInt(st.nextToken()), st.nextToken()));
		}
		
		int X = 0;
		Snake snake = new Snake();
		int headX = 0;
		int headY = 0;
		
		while(true) {
			X++;
			headX += dx[snake.direction];
			headY +=  dy[snake.direction];
//			snake.pos.x += dx[snake.direction];
//			snake.pos.y += dy[snake.direction];
//			snake.body.add(new Position(snake.pos.x, snake.pos.y));
			
			boolean isApple = false;
			
			for(Apple apple: apples) {
				if(headX == apple.pos.x && headY == apple.pos.y) {
//					snake.length++;
					apples.remove(apple);
					isApple = true;
					break;
				}
			}
			
			if(!moves.isEmpty() && moves.peek().time == X) {
				if(moves.peek().direction.equals("L")) {
					snake.direction = (snake.direction + 1)%4;
				}
				else {
					snake.direction = (snake.direction + 3)%4; //(snake.direction + 4 - 1)%4
				}
				moves.remove();
			}
			
			boolean isBody = false;
			if(headX < 0 || headX >= N || headY < 0 || headY >= N) {
				break;
			}
			else {
				for(Position p : snake.body) {
					if (headX == p.x && headY == p.y) {
						isBody = true;
						break;
					}
				}
				if(isBody) break;
				snake.body.add(new Position(headX, headY));
				if(!isApple) snake.body.remove();
			}
		
		}
		System.out.println(X);

	}
	

}

class Snake{
//	int length;
	Position pos;
	int direction;	//0 = right, 1 = up, 2 = left, 3 = down
	Queue<Position> body;
	
	public Snake() {
//		length = 1;
		pos = new Position(0, 0);
		direction = 0;
		body = new LinkedList<>();
		body.add(new Position(0, 0));
	}
}

class Apple{
	Position pos;
	
	public Apple(Position pos) {
		this.pos = pos;
	}
}

class Move{
	int time;
	String direction;
	
	public Move(int time, String direction) {
		this.time = time;
		this.direction = direction;
	}
	
}

class Position{
	int x;
	int y;
	
	public Position(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	public boolean equals(Position other) {
		if (other.x == this.x && other.y == this.y) {
			return true;
		}
		return false;
	}
}