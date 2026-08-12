class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            freq[nums[right]] += 1
            
            # Shrink the window until the current element's frequency is <= k
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            
            # Update max length of valid subarray
            max_len = max(max_len, right - left + 1)
            
        return max_len