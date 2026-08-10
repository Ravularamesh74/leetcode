class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
          
        # dp[i] represents whether the player whose turn it is can win with i stones
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                # If removing k*k stones leaves the other player in a losing state (False),
                # the current player wins (True).
                if not dp[i - k * k]:
                    dp[i] = True
                    break
                k += 1
                
        return dp[n]