class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Add virtual boundary balloons with value 1
        A = [1] + [x for x in nums if x > 0] + [1]
        n = len(A)
        
        # dp[i][j] stores max coins from bursting balloons strictly between i and j
        dp = [[0] * n for _ in range(n)]
        
        # length is the distance between left and right boundary
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][k] + dp[k][right] + A[left] * A[k] * A[right]
                    )
                    
        return dp[0][n - 1]