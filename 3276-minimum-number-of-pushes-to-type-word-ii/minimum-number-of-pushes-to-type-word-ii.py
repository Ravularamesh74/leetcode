from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Count frequency of each letter
        counts = Counter(word)
        
        # Sort frequencies in descending order
        sorted_freqs = sorted(counts.values(), reverse=True)
        
        total_pushes = 0
        
        # Calculate minimum pushes using greedy mapping
        for i, freq in enumerate(sorted_freqs):
            pushes_per_char = (i // 8) + 1
            total_pushes += freq * pushes_per_char
            
        return total_pushes