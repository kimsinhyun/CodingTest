import java.util.*;

class Pg배달 {
    
    public int solution(int N, int[][] road, int K) {
        int answer = 0;

        int[] distance = new int[N+1];
        int[][] graph = new int[N+1][N+1];
        PriorityQueue<int[]> pq = new PriorityQueue<>((e1, e2) -> {
            return e1[1] - e2[1];
        });
        boolean[] visited = new boolean[N+1];
        
        for (int i=0; i<road.length; i++) {
            int a = road[i][0];
            int b = road[i][1];
            int c = road[i][2];
            
            if (graph[a][b] > c || graph[a][b] == 0) {
                graph[a][b] = c;
                graph[b][a] = c;
            }
        }
        
        pq.offer(new int[] {1, 0});
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[1] = 0;
        
        while (!pq.isEmpty()) {
            int cur = pq.poll()[0];
            if (visited[cur]) continue;
            visited[cur] = true;
            
            for (int i=1; i<=N; i++) {
                if (graph[cur][i] != 0 
                    && distance[cur] + graph[cur][i] < distance[i]) {
                    distance[i] = distance[cur] + graph[cur][i];
                    pq.offer(new int[] {i, distance[i]}); 
                }
            }
        }
        
        for (int i=1; i<N+1; i++) {
            if (distance[i] <= K) answer++;
        }

        return answer;
    }
}