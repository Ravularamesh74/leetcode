# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None
        """
        if not root:
            return

        # Flatten left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)

        # Store original right subtree
        temp = root.right

        # Move left subtree to the right
        root.right = root.left
        root.left = None

        # Find the end of the new right subtree
        curr = root
        while curr.right:
            curr = curr.right

        # Attach the original right subtree
        curr.right = temp