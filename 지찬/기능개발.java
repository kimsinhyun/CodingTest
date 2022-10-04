//https://school.programmers.co.kr/learn/courses/30/lessons/42586
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < progresses.length; i++) {
            int days = 0;
            while (progresses[i] + days * speeds[i] < 100) {
                days++;
            }
            queue.add(days);
        }
        ArrayList<Integer> list = new ArrayList<>();
        while (!queue.isEmpty()) {
            Integer poll = queue.poll();
            int cnt = 1;
            while (!queue.isEmpty() && poll >= queue.peek()) {
                cnt++;
                queue.poll();
            }
            list.add(cnt);
        }

        int[] answer = new int[list.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }

    public static void main(String[] args) {
        int[] progresses = {
                93, 30, 55
        };
        int[] speeds = {
                1, 30, 5
        };
        Solution s = new Solution();
        System.out.println(Arrays.toString(s.solution(progresses, speeds)));
    }
}