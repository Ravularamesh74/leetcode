class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = []

        for word in words:
            total = 0
            for ch in word:
                total += weights[ord(ch) - ord('a')]

            mod = total % 26
            # Reverse mapping:
            # 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            mapped = chr(ord('z') - mod)
            result.append(mapped)

        return "".join(result)