//https://school.programmers.co.kr/learn/courses/30/lessons/42584
import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        Stack<Integer> stack = new Stack<>();
        int[] answer = new int[prices.length];
        for (int i = 0; i < prices.length; i++) {
            if (stack.isEmpty()) {
                stack.push(i);
            } else {
                while (!stack.isEmpty() && prices[stack.peek()] > prices[i]) {
                    int idx = stack.pop();
                    answer[idx] = i - idx;
                }
                stack.push(i);
            }
        }
        while (!stack.isEmpty()) {
            int idx = stack.pop();
            answer[idx] = prices.length - 1 - idx;
        }
        return answer;
    }


    public static void main(String[] args) {
        int[] prices = {
                1, 2, 3, 2, 3
        };
        Solution s = new Solution();
        System.out.println(Arrays.toString(s.solution(prices)));
    }
}