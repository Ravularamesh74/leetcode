class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Step 1 & 2: Sort the unique elements and map them to ranks starting from 1
        rank_map = {val: rank for rank, val in enumerate(sorted(set(arr)), 1)}
        
        # Step 3: Replace each element in the original array with its rank
        return [rank_map[num] for num in arr]