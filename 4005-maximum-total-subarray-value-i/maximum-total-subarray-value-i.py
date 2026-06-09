class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mn = nums[0]
        mx = nums[0]
        best = 0

        for x in nums[1:]:
            best = max(best, abs(x - mn), abs(x - mx))
            mn = min(mn, x)
            mx = max(mx, x)

        return best * k