import bisect

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        max_val = max(nums)
        
        # Step 1: Count frequency of each number in nums
        count = [0] * (max_val + 1)
        for x in nums:
            count[x] += 1
            
        # Step 2: For each i, find how many elements in nums are multiples of i
        div_count = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                div_count[i] += count[j]
        
        # Step 3: Compute exact GCD counts using inclusion-exclusion
        gcd_count = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            # Total pairs with GCD as a multiple of i
            total_pairs = div_count[i] * (div_count[i] - 1) // 2
            
            # Subtract pairs with GCD as 2i, 3i, 4i...
            for j in range(2 * i, max_val + 1, i):
                total_pairs -= gcd_count[j]
                
            gcd_count[i] = total_pairs
        
        # Step 4: Build prefix sums of the exact GCD pair counts
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_count[i]
            
        # Step 5: Process queries using binary search
        ans = []
        for q in queries:
            # Find the smallest GCD index g where total cumulative pairs > q
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans