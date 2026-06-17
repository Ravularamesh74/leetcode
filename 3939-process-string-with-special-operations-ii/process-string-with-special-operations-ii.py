class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
       
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        # Length after processing each prefix
        lengths = [0] * (len(s) + 1)

        for i in range(len(s)):
            c = s[i]
            cur = lengths[i]

            if 'a' <= c <= 'z':
                lengths[i + 1] = cur + 1
            elif c == '*':
                lengths[i + 1] = max(0, cur - 1)
            elif c == '#':
                lengths[i + 1] = cur * 2
            else:  # '%'
                lengths[i + 1] = cur

        if k >= lengths[-1]:
            return '.'

        # Walk backwards
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            prev = lengths[i]
            cur = lengths[i + 1]

            if 'a' <= c <= 'z':
                if k == prev:
                    return c
            elif c == '*':
                # Deletion: index unchanged
                pass
            elif c == '#':
                if k >= prev:
                    k -= prev
            else:  # '%'
                k = cur - 1 - k

        return '.'