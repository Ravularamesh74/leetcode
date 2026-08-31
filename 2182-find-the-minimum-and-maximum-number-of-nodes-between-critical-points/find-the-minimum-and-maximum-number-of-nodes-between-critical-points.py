# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        position = 2  # Current node index (1-based)
        
        first_cp = -1
        last_cp = -1
        min_dist = float('inf')
        
        while curr and curr.next:
            # Check if current node is a critical point
            is_maxima = curr.val > prev.val and curr.val > curr.next.val
            is_minima = curr.val < prev.val and curr.val < curr.next.val
            
            if is_maxima or is_minima:
                if first_cp == -1:
                    first_cp = position
                else:
                    # Minimum distance is between adjacent critical points
                    min_dist = min(min_dist, position - last_cp)
                
                last_cp = position
            
            prev = curr
            curr = curr.next
            position += 1
            
        # If less than 2 critical points found
        if first_cp == -1 or first_cp == last_cp:
            return [-1, -1]
        
        max_dist = last_cp - first_cp
        return [min_dist, max_dist]