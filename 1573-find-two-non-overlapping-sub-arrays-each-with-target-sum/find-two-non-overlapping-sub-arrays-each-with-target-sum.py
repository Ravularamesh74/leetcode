class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        inf = float('inf')
        
        # min_len[i] will store the minimum length of a valid subarray in arr[0...i]
        min_len = [inf] * n
        
        ans = inf
        left = 0
        current_sum = 0
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink window if sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
                
            # Valid subarray found ending at right
            if current_sum == target:
                length = right - left + 1
                
                # If a valid non-overlapping subarray exists prior to `left`
                if left > 0 and min_len[left - 1] != inf:
                    ans = min(ans, length + min_len[left - 1])
                
                # Update DP table for current index
                if right > 0:
                    min_len[right] = min(min_len[right - 1], length)
                else:
                    min_len[right] = length
            else:
                # Carry forward the minimum length seen so far
                if right > 0:
                    min_len[right] = min_len[right - 1]
                    
        return ans if ans != inf else -1
