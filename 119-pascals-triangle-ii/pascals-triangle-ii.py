class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Initialize the row with 1 followed by 0s
        row = [1] + [0] * rowIndex
        
        for i in range(1, rowIndex + 1):
            # Update from right to left to use the previous row's values properly
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]
                
        return row