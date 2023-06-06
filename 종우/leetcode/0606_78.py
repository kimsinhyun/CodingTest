# https://leetcode.com/problems/subsets/


# itertools solution
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        for i in range(len(nums)+1):
            for c in combinations(nums, i):
                subset.append(list(c))
        return subset
    
    
# backtracking solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res
