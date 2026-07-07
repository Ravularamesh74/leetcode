class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Extract all non-zero digit characters
        non_zero_digits = [c for c in str(n) if c != '0']
        
        # If there are no non-zero digits, x = 0
        if not non_zero_digits:
            return 0
        
        # Form the new integer x
        x = int("".join(non_zero_digits))
        
        # Calculate the sum of the digits in x
        digit_sum = sum(int(c) for c in non_zero_digits)
        
        # Return x * sum
        return x * digit_sum