# https://leetcode.com/problems/permutations/

# solution using dfs
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        visited = [0]*len(nums)
        def dfs(level, cur):
            if level == len(nums):
                res.append(cur.copy())

            for i in range(len(nums)):
                if not visited[i]:
                    cur.append(nums[i])
                    visited[i] = 1
                    dfs(level+1, cur)
                    cur.pop(-1)
                    visited[i] = 0

        dfs(0, [])
        return res
    

# solution using recursive backtracking...
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            tmp = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(tmp)
            res.extend(perms)
            nums.append(tmp)
            
        return res
