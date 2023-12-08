
class Sol704 {
    public int search(int[] nums, int target) {
      int n = nums.length;
      int l = 0;
      int r = n;

      while (l < r) {
        int m = (l + r) / 2;
        if (nums[m] == target) return m;
        else if (nums[m] > target) {
          r = m; 
        } else {
          l = m+1;
        }
      }
      return -1;
    }
}