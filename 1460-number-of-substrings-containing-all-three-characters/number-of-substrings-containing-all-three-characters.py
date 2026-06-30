class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
       """
        counts = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        ans = 0
        n = len(s)
        
        for right in range(n):
            # Include the current character in the window
            counts[s[right]] += 1
            
            # While the window contains all three characters 'a', 'b', and 'c'
            while counts['a'] > 0 and counts['b'] > 0 and counts['c'] > 0:
                # All substrings from 'right' to the end of the string are valid
                ans += n - right
                
                # Shrink the window from the left
                counts[s[left]] -= 1
                left += 1
                
        return ans