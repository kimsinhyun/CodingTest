class Solution {
    public int jump(int[] nums) {
        int[] dp = new int[nums.length];

        int reached = 0;
        int jumps = 0;

        int start = 0;
        int end = nums[0];
        while (reached < nums.length-1) {
            jumps++;
            for (int i=start+1; i<=end; i++) {
                dp[i] = jumps;
                if (i + nums[i] > reached) {
                    if (i + nums[i] >= nums.length-1) {
                        return jumps +1;
                    }
                    start = i;
                    reached = i + nums[i];
                }
            }
            end = reached;    
        }

        return jumps;
    }
}