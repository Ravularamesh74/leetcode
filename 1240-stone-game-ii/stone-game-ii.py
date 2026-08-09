class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
      
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        
        # Precompute suffix sums: suffix_sum[i] = sum(piles[i:])
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dp(i, m):
            # If all remaining piles can be taken in this turn
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            max_stones = 0
            # Try taking X piles where 1 <= X <= 2 * m
            for x in range(1, 2 * m + 1):
                max_stones = max(
                    max_stones,
                    suffix_sum[i] - dp(i + x, max(m, x))
                )
                
            memo[(i, m)] = max_stones
            return max_stones
        
        return dp(0, 1)