//https://school.programmers.co.kr/learn/courses/30/lessons/72414
class Solution {


    public int toSec(String time) {
        String[] split = time.split(":");
        return Integer.parseInt(split[0]) * 3600 + Integer.parseInt(split[1]) * 60 + Integer.parseInt(split[2]);
    }

    public String toTime(int s) {
        int hour, min, sec;
        sec = s % 60;
        s /= 60;
        min = s % 60;
        s /= 60;
        hour = s;
        return String.format("%02d:%02d:%02d", hour, min, sec);
    }

    public String solution(String play_time, String adv_time, String[] logs) {
        String answer = "";

        int play_time_sec = toSec(play_time);
        int adv_time_sec = toSec(adv_time);

        int[] total = new int[play_time_sec + 1];

        for (String log :
                logs) {
            String[] split = log.split("-");
            int start = toSec(split[0]);
            int end = toSec(split[1]);
            for (int i = start; i < end; i++) {
                total[i]++;
            }
        }

        long sum = 0;
        for (int i = 0; i < adv_time_sec; i++) {
            sum += total[i];
        }

        long longest = sum;
        int longest_start = 0;

        for (int i = 1, j = adv_time_sec; j < play_time_sec; j++, i++) {
            sum += total[j] - total[i - 1];

            if (sum > longest) {
                longest = sum;
                longest_start = i;
            }
        }

        answer = toTime(longest_start);

        return answer;
    }

    public static void main(String[] args) {
        String play_time = "02:03:55";
        String adv_time = "00:14:15";
        String[] logs = {
                "01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"
        };
        Solution solution = new Solution();
        System.out.println(solution.solution(play_time, adv_time, logs));
    }
}
