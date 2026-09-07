class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # end_count[c] stores the count of distinct subsequences ending with character 'c'
        end_count = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            # New subsequences ending in 'char' = 1 (just 'char') + sum of all previous subsequences
            end_count[idx] = (1 + sum(end_count)) % MOD
            
        return sum(end_count) % MOD