class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        cnt = [0, 0, 0]
        for s in stones:
            cnt[s % 3] += 1
            
        c0, c1, c2 = cnt[0], cnt[1], cnt[2]
        
        # If count of 0-remainder stones is even
        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1
        
        # If count of 0-remainder stones is odd
        return abs(c1 - c2) > 2