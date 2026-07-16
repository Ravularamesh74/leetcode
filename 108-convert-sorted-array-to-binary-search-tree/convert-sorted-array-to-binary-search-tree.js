/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    // Helper function to build the tree using a two-pointer range
    function buildBST(left, right) {
        // Base case: if the range is invalid, there are no elements to process
        if (left > right) return null;
        
        // Find the middle element to ensure height balance
        // Using Math.floor((left + right) / 2) avoids overflow issues
        const mid = Math.floor((left + right) / 2);
        
        // Create the root node with the middle value
        const root = new TreeNode(nums[mid]);
        
        // Recursively build the left and right subtrees
        root.left = buildBST(left, mid - 1);
        root.right = buildBST(mid + 1, right);
        
        return root;
    }
    
    return buildBST(0, nums.length - 1);
};