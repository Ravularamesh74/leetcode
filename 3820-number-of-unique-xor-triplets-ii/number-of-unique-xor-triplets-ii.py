class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Extract unique numbers
        unique_nums = set(nums)
        
        # Step 2: Compute all unique pair XOR results
        pair_xors = {x ^ y for x in unique_nums for y in unique_nums}
        
        # Step 3: Compute all unique triplet XOR results
        triplet_xors = {p ^ z for p in pair_xors for z in unique_nums}
        
        return len(triplet_xors)