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
    int ans=0;
    public int cal_height(TreeNode root)
    {
        if(root==null)return 0;
        int lefth = cal_height(root.left);
        int righth= cal_height(root.right);
        ans = Math.max(ans,lefth+righth);
        return 1+Math.max(lefth,righth);
    }
    public int diameterOfBinaryTree(TreeNode root) {
        
        cal_height(root);
        return ans;
    }
}
