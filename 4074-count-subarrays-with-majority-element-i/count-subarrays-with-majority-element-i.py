class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       
        
        n = len(nums)
        ans = 0

        for i in range(n):
            count_target = 0

            for j in range(i, n):
                if nums[j] == target:
                    count_target += 1

                length = j - i + 1

                # target is majority if it appears more than half
                if count_target * 2 > length:
                    ans += 1

        return ans