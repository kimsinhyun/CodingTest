//https://school.programmers.co.kr/learn/courses/30/lessons/92334
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

class Solution {

    HashMap<String, ArrayList<String>> reporters = new HashMap<>();
    HashMap<String, Integer> reported_times = new HashMap<>();

    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        for (String id :
                id_list) {
            reporters.put(id, new ArrayList<>());
            reported_times.put(id, 0);
        }

        for (String r :
                report) {
            String[] s = r.split(" ");
            String reporter = s[0];
            String reported = s[1];
            ArrayList<String> arrayList = reporters.get(reported);
            if(!arrayList.contains(reporter)) {
                arrayList.add(reporter);
                reported_times.put(reported, reported_times.get(reported) + 1);
            }
        }

        for (String key : reported_times.keySet()) {
            if (reported_times.get(key) >= k) {
                for (String id :
                        reporters.get(key)) {
                    for (int i = 0; i < id_list.length; i++) {
                        if (id_list[i].equals(id)) {
                            answer[i]++;
                            break;
                        }
                    }
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] id_list = {
                "muzi", "frodo", "apeach", "neo"
        };
        String[] report = {
                "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"
        };
        int k = 2;
        System.out.println(Arrays.toString(solution.solution(id_list, report, k)));
    }
}