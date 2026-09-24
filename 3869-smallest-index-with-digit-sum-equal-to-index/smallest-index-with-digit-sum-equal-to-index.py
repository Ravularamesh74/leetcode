class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            # Sum the digits of the current number
            digit_sum = sum(int(digit) for digit in str(num))
            
            # Return the first (smallest) index that matches the condition
            if digit_sum == i:
                return i
                
        return -1