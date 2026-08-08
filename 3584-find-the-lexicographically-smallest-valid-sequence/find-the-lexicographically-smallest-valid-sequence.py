class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)
        
        # suffix_match[i] stores the length of the suffix of word2 
        # that can be matched using word1[i:]
        suffix_match = [0] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suffix_match[i] = m - 1 - j

        ans = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break
            
            # Scenario 1: Exact character match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            # Scenario 2: Mismatch, try using our single allowed change
            elif not changed and suffix_match[i + 1] >= m - 1 - j:
                ans.append(i)
                j += 1
                changed = True

        return ans if len(ans) == m else []