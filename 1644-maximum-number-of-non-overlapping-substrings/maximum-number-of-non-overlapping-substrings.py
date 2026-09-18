class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Step 1: Find boundary indices for each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        valid_intervals = []

        # Step 2: Try forming valid intervals starting at first[ch] for each unique char
        for ch in first:
            l = first[ch]
            r = last[ch]
            valid = True
            
            i = l
            while i <= r:
                # Expand right boundary to cover character s[i] fully
                r = max(r, last[s[i]])
                # If s[i] started before l, l is not a valid start
                if first[s[i]] < l:
                    valid = False
                    break
                i += 1
            
            if valid:
                valid_intervals.append((l, r))

        # Step 3: Sort intervals by end position and greedily select non-overlapping ones
        valid_intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1
        
        for l, r in valid_intervals:
            if l > prev_end:
                result.append(s[l:r + 1])
                prev_end = r

        return result