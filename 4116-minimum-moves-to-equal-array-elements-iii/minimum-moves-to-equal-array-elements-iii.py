class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = max(nums)
        return sum(max_val - x for x in nums)