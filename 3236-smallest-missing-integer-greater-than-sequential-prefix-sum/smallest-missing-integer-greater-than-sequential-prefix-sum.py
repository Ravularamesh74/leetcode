class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        # Step 1: Calculate the sum of the longest sequential prefix
        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
            else:
                break

        # Step 2: Convert to set for O(1) lookups
        num_set = set(nums)

        # Step 3: Find the smallest integer >= s missing from nums
        while s in num_set:
            s += 1

        return s