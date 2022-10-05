//https://school.programmers.co.kr/learn/courses/30/lessons/42587
import java.util.Comparator;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
    public int solution(int[] priorities, int location) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        Queue<Integer> queue = new LinkedList<>();
        for (int p :
                priorities) {
            pq.add(p);
            queue.add(p);
        }
        int count = 1;
        while (!queue.isEmpty()) {
            if (pq.peek() == queue.peek()) {
                if (location == 0) {
                    return count;
                }
                pq.poll();
                queue.poll();
                count++;
                location--;
            } else {
                queue.add(queue.poll());
                if (location == 0) {
                    location = queue.size() - 1;
                } else {
                    location--;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int[] priorities = {
                2, 1, 3, 2
        };
        int location = 2;
        Solution s = new Solution();
        System.out.println(s.solution(priorities, location));

    }
}