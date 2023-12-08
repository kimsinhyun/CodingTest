class Sol153 {

    class Solution {
        public int findMin(int[] nums) {
            
            int ln = nums.length;

            if (nums[0] < nums[ln-1]) return nums[0];

            int l = 0;
            int r = ln-1;
            int min = nums[ln-1];
            while(l < r) {
                int m = (l + r) / 2;
                if (nums[m] < min) {
                    min = nums[m];
                    r = m;
                } else {
                    l = m+1;
                }
            }
            
            return min;
        }
    }

}