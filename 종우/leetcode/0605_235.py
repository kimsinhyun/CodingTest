# my solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val:
            return root
        if root.val == q.val:
            return root
        if root.val > p.val:
            if root.val < q.val:
                return root
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val < p.val:
            if root.val > q.val:
                return root
            return self.lowestCommonAncestor(root.right, p, q)
        

# optimized: doesn't have to be recursive
# think of the flip side: cases where 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            else:
                return cur