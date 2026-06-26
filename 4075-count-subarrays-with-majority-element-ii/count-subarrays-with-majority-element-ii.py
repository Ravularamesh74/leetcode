class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        from sortedcontainers import SortedList

        prefix = 0
        ans = 0

        sl = SortedList()
        sl.add(0)

        for num in nums:
            if num == target:
                prefix += 1
            else:
                prefix -= 1

            # Count previous prefix sums that are smaller
            ans += sl.bisect_left(prefix)
            sl.add(prefix)

        return ans