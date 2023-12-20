import java.util.*;

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (e1, e2) -> {
           if (e1[0] == e1[0]) return e1[1] - e2[1];
           return e1[0] - e1[2]; 
        });

        int cnt = 0;
        int mx = -50001;
        for (int i = 0; i<intervals.length; i++) {
            if (intervals[i][0] >= mx) {
                cnt++;
                mx = intervals[i][1];
            } else {
                if (intervals[i][1] < mx) {
                    mx = intervals[i][1];
                }
            }
        } 
        return intervals.length - cnt;
    }
}