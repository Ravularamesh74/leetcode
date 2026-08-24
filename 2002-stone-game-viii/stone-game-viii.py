class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        
        # Compute prefix sums
        pref = stones[:]
        for i in range(1, n):
            pref[i] += pref[i - 1]
            
        # Base case: taking all n stones (index n-1)
        # dp stores the best score difference achievable from the current index onwards
        ans = pref[-1]
        
        # Traverse backwards from index n - 2 down to 1
        # Alice/Bob must pick x > 1, which corresponds to index >= 1 in 0-indexed prefix sums
        for i in range(n - 2, 0, -1):
            ans = max(ans, pref[i] - ans)
            
        return ans