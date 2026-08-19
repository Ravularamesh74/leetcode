class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_set = set(wordDict)  # Convert to set for O(1) lookups
        memo = {}

        def backtrack(start):
            # If we reached the end of the string, return an empty string representation
            if start == len(s):
                return [""]
            
            # Return cached result if already computed
            if start in memo:
                return memo[start]
            
            res = []
            # Try forming words starting from index 'start'
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Recursively get all valid sentences for the remaining substring
                    sub_sentences = backtrack(end)
                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)
            
            memo[start] = res
            return res

        return backtrack(0)