# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None
        """
        self.first = None
        self.second = None
        self.prev = None

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev and self.prev.val > node.val:
                if self.first is None:
                    self.first = self.prev
                self.second = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        self.first.val, self.second.val = self.second.val, self.first.val