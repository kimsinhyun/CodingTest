# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# tree data structure

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    answer = 0
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            self.dfs(1, root)
        return self.answer

    def dfs(self, depth, node):
        if depth > self.answer:
            self.answer = depth
        if node.left:
            self.dfs(depth+1, node.left)
        if node.right:
            self.dfs(depth+1, node.right)