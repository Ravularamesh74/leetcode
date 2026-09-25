class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Start with a copy of the bottom row
        dp = list(triangle[-1])
        
        # Bottom-up approach: iterate from second-to-last row up to the top
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Minimum path at current cell is its value + min of two adjacent values below
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
                
        return dp[0]