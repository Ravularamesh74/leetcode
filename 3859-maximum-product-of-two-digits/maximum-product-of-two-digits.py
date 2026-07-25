class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Convert n to a list of integer digits sorted in descending order
        digits = sorted([int(d) for d in str(n)], reverse=True)
        
        # Return the product of the two largest digits
        return digits[0] * digits[1]