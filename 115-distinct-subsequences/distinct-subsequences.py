class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        if m < n:
            return 0

        # dp[j] stores the number of subsequences matching t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty string t can always be formed once

        for char in s:
            for j in range(n, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]