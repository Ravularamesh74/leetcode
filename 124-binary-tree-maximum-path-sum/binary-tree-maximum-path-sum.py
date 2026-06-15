# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = float("-inf")

        def dfs(node):
            if not node:
                return 0

            # Ignore negative contributions
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Path passing through this node
            self.ans = max(self.ans, node.val + left + right)

            # Return the best one-sided path
            return node.val + max(left, right)

        dfs(root)
        return self.ans