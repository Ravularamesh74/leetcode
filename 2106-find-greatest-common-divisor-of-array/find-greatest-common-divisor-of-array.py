class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the smallest and largest numbers
        min_num = min(nums)
        max_num = max(nums)
        
        # Apply Euclid's algorithm to find the GCD
        while min_num:
            max_num, min_num = min_num, max_num % min_num
            
        return max_num