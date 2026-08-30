class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n

        # Find indices of minimum and maximum elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Ensure i is the smaller index and j is the larger index
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)

        # 3 possible strategies:
        # 1. Delete both from front up to j
        both_front = j + 1
        # 2. Delete both from back starting from i
        both_back = n - i
        # 3. Delete one from front up to i, and one from back starting from j
        front_and_back = (i + 1) + (n - j)

        return min(both_front, both_back, front_and_back)