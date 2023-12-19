// my attempt: fail
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        if (intervals.length == 0) {
            return new int[][] {newInterval};
        }
        List<int[]> ans = new ArrayList<>();
        
        for (int i=0; i<intervals.length; i++) {
            if (intervals[i][0] < newInterval[0] && intervals[i][1] < newInterval[0]) {
                ans.add(intervals[i]);
            } else if (intervals[i][0] < newInterval[0] && newInterval[0] <= intervals[i][1]) {
                int next = intervals.length;
                // starting in between 
                if (newInterval[1] <= intervals[i][1]) {
                    ans.add(intervals[i]);
                    next = i+1;
                } else {
                    if (i == intervals.length-1) {
                        ans.add(new int[] {intervals[i][0], newInterval[1]});
                    }
                    for (int j=i+1; j<intervals.length; j++) {
                        if (newInterval[1] < intervals[j][0]) {
                            ans.add(new int[] {intervals[i][0], newInterval[1]});
                            next = j;
                            break;
                        } else if (newInterval[1] <= intervals[j][1]) {
                            ans.add(new int[] {intervals[i][0], intervals[j][1]});
                            next = j+1;
                            break;
                        }
                    }
                    
                }
                for (int j=next; j<intervals.length; j++) {
                    ans.add(intervals[j]);
                }
                break;
            } else if (newInterval[0] < intervals[i][0] && intervals[i][0] <= newInterval[1]) {
                // starting in between 
                int next = intervals.length;
                if (intervals[i][1] <= newInterval[1]) {
                    ans.add(intervals[i]);
                    next = i+1;
                } else {
                    if (i == intervals.length-1) {
                        ans.add(new int[] {intervals[i][0], newInterval[1]});
                    }
                    for (int j=i+1; j<intervals.length; j++) {
                        if (newInterval[1] < intervals[j][0]) {
                            ans.add(new int[] {intervals[i][0], newInterval[1]});
                            next = j;
                            break;
                        } else if (newInterval[1] <= intervals[j][1]) {
                            ans.add(new int[] {intervals[i][0], intervals[j][1]});
                            next = j+1;
                            break;
                        }
                    }
                  
                }
                for (int j=next; j<intervals.length; j++) {
                    ans.add(intervals[j]);
                }
                break;
            } else if (newInterval[1] < intervals[i][0]) {
                ans.add(newInterval);
                for (int j=i; j<intervals.length; j++) {
                    ans.add(intervals[j]);
                }
                break;
            }
        }
        return ans.toArray(new int[ans.size()][2]);
    }
}