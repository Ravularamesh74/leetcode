from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        ans = 0
        
        # 1. Handle the edge case of 1s separately
        if 1 in freq:
            count = freq[1]
            # The length must be odd, so if it's even, take count - 1
            ans = count if count % 2 != 0 else count - 1
            
        # 2. Process all other numbers > 1
        for x in freq:
            if x == 1:
                continue
                
            current_length = 0
            val = x
            
            # Keep climbing the squaring chain as long as we have at least 2 copies
            while freq[val] >= 2:
                current_length += 2
                val *= val
                
            # Now 'val' is the peak element. We need at least 1 copy to finish the sequence.
            if freq[val] >= 1:
                current_length += 1
            else:
                # If the peak element doesn't exist, we must back off the last layer's peak
                current_length -= 1
                
            ans = max(ans, current_length)
            
        return ans