/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val === undefined ? 0 : val)
 *     this.left = (left === undefined ? null : left)
 *     this.right = (right === undefined ? null : right)
 * }
 */

/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    let ans = [];

    function inorder(node) {
        if (node === null) return;

        inorder(node.left);     // Left
        ans.push(node.val);     // Root
        inorder(node.right);    // Right
    }

    inorder(root);

    return ans;
};