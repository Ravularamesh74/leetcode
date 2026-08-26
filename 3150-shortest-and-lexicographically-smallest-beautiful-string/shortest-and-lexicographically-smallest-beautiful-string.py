class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if s.count('1') < k:
            return ""
        
        # Collect indices of all '1's in string s
        ones_indices = [i for i, char in enumerate(s) if char == '1']
        
        res = ""
        min_len = float('inf')
        
        # Sliding window over the indices of '1's
        for i in range(len(ones_indices) - k + 1):
            start = ones_indices[i]
            end = ones_indices[i + k - 1]
            sub = s[start:end + 1]
            
            # Update best candidate if it's shorter or lexicographically smaller
            if len(sub) < min_len:
                min_len = len(sub)
                res = sub
            elif len(sub) == min_len and sub < res:
                res = sub
                
        return res