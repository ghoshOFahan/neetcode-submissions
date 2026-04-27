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
    int ans = 0;
    public int calculate_height(TreeNode root){
        if(root==null) return 0;
        int lefth = calculate_height(root.left);
        int righth = calculate_height(root.right);
        ans = Math.max(ans,lefth+righth);
        return 1+Math.max(lefth,righth);
    }
    public int diameterOfBinaryTree(TreeNode root) {
        calculate_height(root);
        return ans;
    }
}
