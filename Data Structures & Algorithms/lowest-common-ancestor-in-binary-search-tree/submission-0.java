/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root==null) return null;
        if(root.val==p.val||root.val==q.val) return root;
        TreeNode leftlca = lowestCommonAncestor(root.left,p,q);
        TreeNode rightlca = lowestCommonAncestor(root.right,p,q);
        if(leftlca==null && rightlca==null) return null;
        else if(leftlca==null) return rightlca;
        else if(rightlca==null) return leftlca;
        else return root;
    }
}
