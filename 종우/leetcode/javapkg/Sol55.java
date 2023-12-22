class Solution {
    public boolean canJump(int[] nums) {
        int dest = 0;
        for (int i=0; i<nums.length; i++) {

            if (i > dest) return false;

            dest = Math.max(i+nums[i], dest);

            if (dest >= nums.length - 1) return true;
        }
        
        return true;
    }
}