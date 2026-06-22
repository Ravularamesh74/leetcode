class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
       
        count = {}

        for ch in text:
            count[ch] = count.get(ch, 0) + 1

        return min(
            count.get('b', 0),
            count.get('a', 0),
            count.get('l', 0) // 2,
            count.get('o', 0) // 2,
            count.get('n', 0)
        )