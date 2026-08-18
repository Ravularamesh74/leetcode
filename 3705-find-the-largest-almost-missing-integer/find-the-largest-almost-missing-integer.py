class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        subarray_count = {}
        
        # Iterate over all subarrays of size k
        for i in range(n - k + 1):
            # Find unique elements in the current subarray
            unique_in_sub = set(nums[i:i + k])
            for num in unique_in_sub:
                subarray_count[num] = subarray_count.get(num, 0) + 1
        
        # Find the largest integer that appears in exactly one subarray of size k
        ans = -1
        for num, count in subarray_count.items():
            if count == 1:
                ans = max(ans, num)
                
        return ans