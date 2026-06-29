class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        
        def is_substring(p, w):
            # If the pattern is longer than the word, it can't be a substring
            if len(p) > len(w):
                return False
            
            # Check every starting position in the word
            for i in range(len(w) - len(p) + 1):
                if w[i:i+len(p)] == p:
                    return True
            return False

        count = 0
        for p in patterns:
            if is_substring(p, word):
                count += 1
                
        return count