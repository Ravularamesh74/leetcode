from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        st1 = Counter(ransomNote)
        st2 = Counter(magazine)
        
        for char, count in st1.items():
            if st2[char] < count:
                return False
                
        return True