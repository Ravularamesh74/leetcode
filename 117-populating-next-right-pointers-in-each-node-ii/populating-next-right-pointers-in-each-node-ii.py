"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        # Start with the root level
        current = root
        
        while current:
            # Dummy node to anchor the start of the next level
            dummy = Node(0)
            tail = dummy
            
            # Traverse the current level using established next pointers
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                # Move to the next node in the current level
                current = current.next
            
            # Move down to the head of the newly populated level
            current = dummy.next
            
        return root