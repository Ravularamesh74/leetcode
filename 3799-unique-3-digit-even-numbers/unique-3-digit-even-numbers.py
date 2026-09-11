class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        counts = Counter(digits)
        valid_count = 0
        
        # Check all possible 3-digit even numbers
        for num in range(100, 1000, 2):
            d1 = num // 100        # Hundreds digit
            d2 = (num // 10) % 10  # Tens digit
            d3 = num % 10          # Units digit
            
            num_counts = Counter([d1, d2, d3])
            
            # Check if we have enough copies of each required digit
            if all(counts[d] >= num_counts[d] for d in num_counts):
                valid_count += 1
                
        return valid_count