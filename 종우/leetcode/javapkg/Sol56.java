import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (e1, e2) -> {
            return e1[0] - e2[0];
        });

        List<int[]> ans = new ArrayList<>();
        int[] merge = intervals[0]; 

        for (int i=1; i<intervals.length; i++) {
            if (merge[1] < intervals[i][0]) {
                ans.add(merge);
                merge = intervals[i];
            } else {
                merge[1] = Math.max(merge[1], intervals[i][1]);
            }
        }
        ans.add(merge);

        return ans.toArray(new int[ans.size()][2]);
    }
}