# https://leetcode.com/problems/binary-tree-right-side-view/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# using dfs
class Solution:
    depth = 0
    def rightSideView(self, root: TreeNode) -> list[int]:
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
    

# using bfs / level order traversal
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        from collections import deque

        res = []
        dq = deque([root])

        while dq:  
            # pop and add rest
            rightMost = None
            l = len(dq)

            for i in range(l):
                cur = dq.popleft()
                if cur:
                    rightMost = cur
                    dq.append(cur.left)
                    dq.append(cur.right)
            if rightMost:
                res.append(rightMost.val)
        return res