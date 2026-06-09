class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        leftmost = root

        while leftmost.left:
            curr = leftmost

            while curr:
                # Connect left child -> right child
                curr.left.next = curr.right

                # Connect right child -> next node's left child
                if curr.next:
                    curr.right.next = curr.next.left

                curr = curr.next

            leftmost = leftmost.left

        return root