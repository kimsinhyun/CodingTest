//https://school.programmers.co.kr/learn/courses/30/lessons/12909
import java.util.Stack;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c :
                s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
            }
        }

        if (!stack.isEmpty()) {
            return false;
        }


        return true;
    }

    public static void main(String[] args) {
        String s = "()()";
        Solution solution = new Solution();
        System.out.println(solution.solution(s));
    }
}