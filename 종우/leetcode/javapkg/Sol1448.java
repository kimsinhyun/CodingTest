class Sol1448 {
    //  Definition for a binary tree node.
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    private int cnt;
    public int goodNodes(TreeNode root) {
        cnt = 0;

        dfs(Integer.MIN_VALUE, root);
        
        return cnt;
    }
    
    private void dfs(int max, TreeNode cur) {

        if (cur.val >= max) {
            cnt++;
            max = cur.val;
        }

        if (cur.left != null) {
            dfs(max, cur.left);
        }

        if (cur.right != null) {
            dfs(max, cur.right);
        }
    }
}