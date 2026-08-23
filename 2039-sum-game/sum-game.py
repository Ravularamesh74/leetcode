class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        half = n // 2
        
        left_str = num[:half]
        right_str = num[half:]
        
        left_sum = sum(int(c) for c in left_str if c != '?')
        right_sum = sum(int(c) for c in right_str if c != '?')
        
        left_q = left_str.count('?')
        right_q = right_str.count('?')
        
        # If the total number of '?' is odd, Alice always gets the last move and wins.
        if (left_q + right_q) % 2 != 0:
            return True
        
        # For Bob to win, the difference in sums must equal 4.5 * (right_q - left_q)
        return (left_sum - right_sum) != (right_q - left_q) * 4.5