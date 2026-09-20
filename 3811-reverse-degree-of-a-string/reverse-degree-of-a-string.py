class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i, char in enumerate(s, 1):
            reversed_alphabet_pos = 26 - (ord(char) - ord('a'))
            total += reversed_alphabet_pos * i
        return total