import math

class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        max_val = max(nums)
        
        # Memoization dictionary
        memo = {}
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def solve(i, g1, g2):
            # Base case: if we have processed all elements
            if i == n:
                # Both subsequences must be non-empty (GCD > 0) and have equal GCD
                return 1 if g1 == g2 and g1 > 0 else 0
            
            state = (i, g1, g2)
            if state in memo:
                return memo[state]
            
            # Option 1: Skip the current element
            ans = solve(i + 1, g1, g2)
            
            # Option 2: Put nums[i] into seq1
            ans = (ans + solve(i + 1, gcd(g1, nums[i]), g2)) % MOD
            
            # Option 3: Put nums[i] into seq2
            ans = (ans + solve(i + 1, g1, gcd(g2, nums[i]))) % MOD
            
            memo[state] = ans
            return ans
        
        return solve(0, 0, 0)