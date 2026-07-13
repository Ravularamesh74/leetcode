class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        sample = "123456789"
        result = []
        
        # Determine the length of digits to look for
        min_len = len(str(low))
        max_len = len(str(high))
        
        # Iterate over all valid lengths
        for length in range(min_len, max_len + 1):
            # Slide a window of 'length' over the sample string
            for start in range(10 - length):
                num = int(sample[start:start + length])
                if low <= num <= high:
                    result.append(num)
                    
        return result