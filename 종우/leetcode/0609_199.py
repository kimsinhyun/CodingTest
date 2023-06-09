# https://leetcode.com/problems/binary-tree-right-side-view/

class Solution:
    depth = 0
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(level, cur):
            if cur == None:
                return

            if level >= self.depth:
                res.append(cur.val)
                self.depth += 1
            
            dfs(level+1, cur.right)
            dfs(level+1, cur.left)
        
        
        dfs(0, root)
        return res