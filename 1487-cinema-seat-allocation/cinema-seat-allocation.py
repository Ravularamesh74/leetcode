class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict


        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        # Map row -> bitmask representing reserved seats (2 through 9)
        rows = defaultdict(int)
        
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                # Store seat presence using bitshift relative to seat 2
                rows[r] |= (1 << (c - 2))
                
        # Bitmasks for seat blocks (relative to seats 2..9):
        # Seats 2, 3, 4, 5 -> positions 0, 1, 2, 3 -> binary 0000 1111 (0b00001111 / 15)
        # Seats 6, 7, 8, 9 -> positions 4, 5, 6, 7 -> binary 1111 0000 (0b11110000 / 240)
        # Seats 4, 5, 6, 7 -> positions 2, 3, 4, 5 -> binary 0011 1100 (0b00111100 / 60)
        left_mask = 0b00001111
        right_mask = 0b11110000
        mid_mask = 0b00111100
        
        # Start by assuming all rows can hold 2 families
        ans = (n - len(rows)) * 2
        
        for mask in rows.values():
            placed = 0
            
            # Check left block (2, 3, 4, 5)
            if not (mask & left_mask):
                placed += 1
                
            # Check right block (6, 7, 8, 9)
            if not (mask & right_mask):
                placed += 1
                
            # If neither left nor right block could be placed, check middle block (4, 5, 6, 7)
            if placed == 0 and not (mask & mid_mask):
                placed = 1
                
            ans += placed
            
        return ans