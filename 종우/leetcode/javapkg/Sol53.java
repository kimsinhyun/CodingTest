class Solution {
    public int maxSubArray(int[] nums) {
        int max = Integer.MIN_VALUE;
        int cursum = 0;
        int prevsum = 0;
        for (int i=0; i<nums.length; i++) {
            if (prevsum < 0) {
                cursum -= prevsum;
                prevsum = 0;
            } 
            cursum += nums[i];
            if (cursum > max) max = cursum;
            prevsum = cursum;
        }
        return max;
    }
}