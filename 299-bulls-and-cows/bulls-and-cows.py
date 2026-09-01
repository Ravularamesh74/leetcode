from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        secret_counts = Counter()
        guess_counts = Counter()
        
        # Step 1: Count bulls and store unmatched characters
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_counts[s] += 1
                guess_counts[g] += 1
                
        # Step 2: Count cows by finding common remaining characters
        cows = sum(min(secret_counts[ch], guess_counts[ch]) for ch in secret_counts)
        
        # Step 3: Return formatted result string
        return "{0}A{1}B".format(bulls, cows)