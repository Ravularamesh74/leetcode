class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Augment s with '1' on both sides as per the problem description
        t = '1' + s + '1'
        
        # Group contiguous identical characters into (char, length) tuples
        blocks = []
        i = 0
        n = len(t)
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j
            
        initial_ones = s.count('1')
        max_delta = 0
        
        # Look for '1' blocks surrounded by '0' blocks
        for k in range(1, len(blocks) - 1):
            if blocks[k][0] == '1':
                # Check if it is surrounded by '0' blocks on both sides
                if blocks[k - 1][0] == '0' and blocks[k + 1][0] == '0':
                    delta = blocks[k - 1][1] + blocks[k + 1][1]
                    max_delta = max(max_delta, delta)
                    
        return initial_ones + max_delta