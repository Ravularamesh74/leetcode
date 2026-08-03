class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp = [0] * (n + 1)
        
        # Iterate backwards from the end of the stoneValue array
        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            take_sum = 0
            
            # Try taking 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k <= n:
                    take_sum += stoneValue[i + k - 1]
                    dp[i] = max(dp[i], take_sum - dp[i + k])
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"