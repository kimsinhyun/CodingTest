# https://leetcode.com/problems/combination-sum/

# initial solve (barely passed) using backtracking
# maybe another solution using iterator.combinations
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        cur = []
        
        def dfs():
            s = sum(cur)
            if s == target:
                tmp = cur.copy()
                tmp.sort()
                if tmp not in res:
                    res.append(tmp)
                return
            elif s > target:
                return
            
            for c in candidates:
                cur.append(c)
                dfs()
                cur.pop()

        dfs()
        return res
    

# optimized
# 1. don't sum every recursive call, but track sum using argument variables
# 2. don't remove duplicates, but prevent them by adding next candidate
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i > len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res
