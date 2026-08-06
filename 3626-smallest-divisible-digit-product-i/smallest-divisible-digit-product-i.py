class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            # Calculate product of digits
            prod = 1
            temp = n
            while temp > 0:
                prod *= temp % 10
                temp //= 10
            
            # Check divisibility
            if prod % t == 0:
                return n
            
            n += 1