class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Calculate C(n + k - 1, 2 * k) % MOD
        N = n + k - 1
        R = 2 * k
        
        if R > N:
            return 0
        
        num = 1
        den = 1
        for i in range(1, R + 1):
            num = (num * (N - i + 1)) % MOD
            den = (den * i) % MOD
            
        return (num * pow(den, MOD - 2, MOD)) % MOD