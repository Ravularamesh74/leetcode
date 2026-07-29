class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        from collections import Counter

        n = len(s)
        cnt = Counter(s)
        
        # Calculate half counts for the first half
        half_cnt = {c: cnt[c] // 2 for c in cnt}
        m = n // 2
        
        # Identify middle character if string length is odd
        mid_char = ""
        for c in cnt:
            if cnt[c] % 2 != 0:
                mid_char = c
                break

        # Function to calculate number of unique permutations of remaining characters
        # Capped at k to prevent integer overflow/unnecessary large computations
        def count_permutations(counts, cap):
            total_len = sum(counts.values())
            res = 1
            # We can build combination incrementally: res = L! / (c1! * c2! ... )
            # Using Pascal's formula or nCr incrementally
            curr_len = 0
            for char_count in counts.values():
                for i in range(1, char_count + 1):
                    curr_len += 1
                    res = (res * curr_len) // i
                    if res > cap:
                        return cap + 1
            return res

        # Check if total possible permutations is less than k
        total_possible = count_permutations(half_cnt, k)
        if total_possible < k:
            return ""

        # Construct the left half character by character
        left_half = []
        
        for _ in range(m):
            for ch in sorted(half_cnt.keys()):
                if half_cnt[ch] > 0:
                    # Try picking character `ch`
                    half_cnt[ch] -= 1
                    ways = count_permutations(half_cnt, k)
                    
                    if ways >= k:
                        left_half.append(ch)
                        break
                    else:
                        k -= ways
                        half_cnt[ch] += 1  # Backtrack and try next character

        left_str = "".join(left_half)
        right_str = left_str[::-1]
        
        return left_str + mid_char + right_str