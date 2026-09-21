class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        # dp[r] will store the number of subarrays ending at the current index
        # whose product modulo k is r.
        dp = [0] * k
        
        for num in nums:
            mod_val = num % k
            next_dp = [0] * k
            
            # Subarray consisting of just the current element
            next_dp[mod_val] += 1
            
            # Extend previous subarrays ending at index - 1
            for r in range(k):
                if dp[r] > 0:
                    next_r = (r * mod_val) % k
                    next_dp[next_r] += dp[r]
            
            # Accumulate current subarray counts to the total result
            for r in range(k):
                ans[r] += next_dp[r]
                
            dp = next_dp
            
        return ans