//https://school.programmers.co.kr/learn/courses/30/lessons/72413
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    class Edge{
        public int cost;
        public int vertex;

        public Edge(int vertex, int cost) {
            this.cost = cost;
            this.vertex = vertex;
        }
    }

    class Node implements Comparable<Node> {
        public int vertex;
        public int weight;

        public Node(int vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return this.weight - o.weight;
        }
    }


    public int solution(int n, int s, int a, int b, int[][] fares) {
        ArrayList<Edge>[] graph = new ArrayList[n];
        for (int i = 0; i < graph.length; i++) {
            graph[i] = new ArrayList<>();
        }
        int[] together = new int[n];
        int[] aloneA = new int[n];
        int[] aloneB = new int[n];
        for (int i = 0; i < fares.length; i++) {
            graph[fares[i][0] - 1].add(new Edge(fares[i][1] - 1, fares[i][2]));
            graph[fares[i][1] - 1].add(new Edge(fares[i][0] - 1, fares[i][2]));
        }

        together = dijkstra(s - 1, graph, together);
        aloneA = dijkstra(a - 1, graph, aloneA);
        aloneB = dijkstra(b - 1, graph, aloneB);

        int minimum = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (minimum > together[i] + aloneA[i] + aloneB[i]) {
                minimum = together[i] + aloneA[i] + aloneB[i];
            }
        }
        return minimum;
    }

    private int[] dijkstra(int start, ArrayList<Edge>[] graph, int[] arr) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        Arrays.fill(arr, Integer.MAX_VALUE);
        pq.add(new Node(start, 0));
        arr[start] = 0;
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            if(node.weight > arr[node.vertex]) continue;
            for(Edge e : graph[node.vertex]) {
                if (arr[e.vertex] > node.weight + e.cost) {
                    arr[e.vertex] = node.weight + e.cost;
                    pq.add(new Node(e.vertex, arr[e.vertex]));
                }
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        int n=7, s=3, a=4, b=1;
        int[][] fares = {
                {5, 7, 9}, {4, 6, 4}, {3, 6, 1}, {3, 2, 3}, {2, 1, 6}
        };
        Solution solution = new Solution();
        System.out.println(solution.solution(n, s, a, b, fares));
    }
}