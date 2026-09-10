# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.matching_nodes = 0

        def dfs(node):
            if not node:
                return 0, 0  # (sum, count)
            
            # Post-order traversal: process subtrees first
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Current subtree total sum and count
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            
            # Check if average (integer division) equals node value
            if total_sum // total_count == node.val:
                self.matching_nodes += 1
                
            return total_sum, total_count

        dfs(root)
        return self.matching_nodes