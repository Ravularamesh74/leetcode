class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        min_odd = float('inf')
        
        # Find the smallest odd element
        for num in nums1:
            if num % 2 != 0:
                min_odd = min(min_odd, num)
                
        # If there are no odd numbers, all elements are already even -> True
        if min_odd == float('inf'):
            return True
        
        # Check if every even number is strictly greater than min_odd
        for num in nums1:
            if num % 2 == 0 and num < min_odd:
                return False
                
        return True