import java.util.*;

// my solution time: 16%
class Sol90 {
    List<List<Integer>> ans = new ArrayList<>();
    Set<List<Integer>> power = new HashSet<>();
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        
        dfs(0, new ArrayDeque<>(), nums);
        
        return ans;
    }

    private void dfs(int cnt, ArrayDeque<Integer> tmp, int[] nums) {

        if (cnt == nums.length) {
            List<Integer> subset = new ArrayList<>();
            for (int i: tmp) {
                subset.add(i);
            }
            subset.sort(Comparator.naturalOrder());
            if (!power.contains(subset)) {
                power.add(subset);
                ans.add(subset);
            }

            return;
        } 

        dfs(cnt+1, tmp, nums);
        tmp.offerLast(nums[cnt]);
        dfs(cnt+1, tmp, nums);
        tmp.pollLast();

    }
}

// optimized solution: only uses lists, not using sets, just skipping duplicates
class Solution2 {
    List<List<Integer>> ans = new ArrayList<>();
    List<Integer> tmp = new ArrayList<>();
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {

        Arrays.sort(nums);
        dfs(0, nums);
        
        return ans;
    }

    private void dfs(int cnt, int[] nums) {

        if (cnt == nums.length) {
            ans.add(new ArrayList<>(tmp));
            return;
        }

        tmp.add(nums[cnt]);
        dfs(cnt+1, nums);
        tmp.remove(tmp.size()-1);

        while (cnt + 1 < nums.length && nums[cnt] == nums[cnt+1]) cnt++;
        dfs(cnt+1, nums);

    }
}