class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        half_len = n // 2
        
        # Sort the first half of the string to get the smallest prefix
        left_half = sorted(s[:half_len])
        
        # Middle character for odd lengths
        mid = s[half_len] if n % 2 != 0 else ""
        
        # Construct the palindrome
        return "".join(left_half) + mid + "".join(reversed(left_half))