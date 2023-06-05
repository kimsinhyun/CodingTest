# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first try
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        if root.left != None:
            self.invertTree(root.left)
        if root.right != None:
            self.invertTree(root.right)
        tmp = root.right
        root.right = root.left
        root.left = tmp
        return root
    

# optimized
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        tmp = root.right
        root.right = root.left
        root.left = tmp
        return root