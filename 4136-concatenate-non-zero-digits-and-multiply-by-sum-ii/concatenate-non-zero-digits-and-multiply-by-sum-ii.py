import bisect

class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        
        # Gather non-zero digits and their original positions
        nz_indices = []
        nz_digits = []
        
        for i, ch in enumerate(s):
            if ch != '0':
                nz_indices.append(i)
                nz_digits.append(int(ch))
                
        n = len(nz_digits)
        if n == 0:
            return [0] * len(queries)
            
        # Precompute prefix sum for digit sums
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + nz_digits[i]
            
        # Precompute prefix values for concatenated numbers modulo 10^9 + 7
        pref_val = [0] * (n + 1)
        for i in range(n):
            pref_val[i + 1] = (pref_val[i] * 10 + nz_digits[i]) % MOD
            
        # Precompute powers of 10 modulo 10^9 + 7
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        ans = []
        for l, r in queries:
            # Find the segment of non-zero elements that fall within [l, r]
            L = bisect.bisect_left(nz_indices, l)
            R = bisect.bisect_right(nz_indices, r) - 1
            
            if L > R:
                ans.append(0)
                continue
                
            # Number of non-zero digits in this query range
            count = R - L + 1
            
            # Extract x % MOD
            x = (pref_val[R + 1] - pref_val[L] * pow10[count]) % MOD
            
            # Extract sum of digits
            s_digits = pref_sum[R + 1] - pref_sum[L]
            
            # Calculate final answer for the query
            ans.append((x * s_digits) % MOD)
            
        return ans