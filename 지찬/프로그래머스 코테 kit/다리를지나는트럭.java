//https://school.programmers.co.kr/learn/courses/30/lessons/42583
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    class Truck {
        int weight;
        int time;

        public Truck(int weight, int time) {
            this.weight = weight;
            this.time = time;
        }
    }
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> bridge = new LinkedList<>();
        int sum = 0;
        int sec = 0;
        for (int t :
                truck_weights) {
            while (true) {
                if (bridge.isEmpty()) {
                    sum += t;
                    bridge.add(t);
                    sec++;
                    break;
                } else if (bridge.size() == bridge_length) {
                    sum -= bridge.poll();
                } else {
                    if (sum + t > weight) {
                        bridge.add(0);
                        sec++;
                    } else {
                        bridge.add(t);
                        sum += t;
                        sec++;
                        break;
                    }
                }
            }

        }
        return sec + bridge_length;
    }

    public static void main(String[] args) {
        int[] truck_weights = {
                7, 4, 5, 6
        };
        Solution s = new Solution();
        System.out.println(s.solution(2, 10, truck_weights));
    }
}