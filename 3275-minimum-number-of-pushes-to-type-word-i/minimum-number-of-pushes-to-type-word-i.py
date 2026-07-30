
class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        pushes = 0
        
        for i in range(n):
            # i // 8 gives the 0-indexed key position layer (0, 1, 2, 3)
            # Add 1 to convert it to actual pushes needed per character
            pushes += (i // 8) + 1
            
        return pushes