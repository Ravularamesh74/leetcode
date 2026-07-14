class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        if valueDiff < 0:
            return False
        
        buckets = {}
        # Width of each bucket
        w = valueDiff + 1
        
        for i, num in enumerate(nums):
            # Get the bucket identifier
            bucket_id = num // w
            
            # Case 1: Same bucket already has an item within the index window
            if bucket_id in buckets:
                return True
                
            # Case 2: Check the left neighbor bucket
            if (bucket_id - 1) in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
                
            # Case 3: Check the right neighbor bucket
            if (bucket_id + 1) in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
            
            # Put the current number into its bucket
            buckets[bucket_id] = num
            
            # Maintain sliding window of size indexDiff
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // w
                del buckets[old_bucket_id]
                
        return False