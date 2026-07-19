class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Find the last occurrence index of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            # If character is already in our current subsequence, skip it
            if char in seen:
                continue
                
            # Pop characters from stack if they are larger than the current character
            # AND they appear later in the remaining part of the string
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            # Add the current character to both stack and seen set
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)