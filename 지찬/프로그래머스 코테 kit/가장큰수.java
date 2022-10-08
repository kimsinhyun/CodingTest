//https://school.programmers.co.kr/learn/courses/30/lessons/42746
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    class StringComparator implements Comparator<String> {

        @Override
        public int compare(String o1, String o2) {
            return (o2 + o1).compareTo(o1 + o2);
        }
    }
    public String solution(int[] numbers) {
        String answer = "";

        String[] strings = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            strings[i] = String.valueOf(numbers[i]);
        }
        Comparator<String> StringComparator = new StringComparator();
        Arrays.sort(strings, StringComparator);
        for (String s :
                strings) {
            answer += s;
        }
        return answer.startsWith("0") ? "0" : answer;
    }

    public static void main(String[] args) {
        int[] numbers = {
                6, 10, 2
        };
        Solution s = new Solution();
        System.out.println(s.solution(numbers));
    }
}