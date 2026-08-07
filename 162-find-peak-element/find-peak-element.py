class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the right neighbor is greater, a peak must exist on the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # Otherwise, a peak must exist at mid or on the left
            else:
                right = mid
                
        return left