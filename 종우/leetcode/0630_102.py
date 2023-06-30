# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# tree level order traversal

# solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        from collections import deque

        res = []
        dq = deque()

        if root:
            dq.append(root)

        while dq:
            level = []
            width = len(dq)

            for i in range(width):
                cur = dq.popleft()
                level.append(cur.val)
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            res.append(level)
        return res