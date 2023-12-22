class Solution {
    public int jump(int[] nums) {
        int[] dp = new int[nums.length];

        int cnt = 0;
        int jumps = 0;

        int start = 0;
        int end = Math.min(nums.length-1, nums[0]);
        while (cnt < nums.length-1) {
            jumps++;
            int reached = end;
            for (int i=start+1; i<=end; i++) {
                dp[i] = jumps;
                if (i + nums[i] > reached) {
                    start = i;
                    reached = i + nums[i];
                }
            }
            cnt = end;
            start = end;
            end = Math.min(reached, nums.length-1);
        }

        return dp[nums.length-1];
    }
}