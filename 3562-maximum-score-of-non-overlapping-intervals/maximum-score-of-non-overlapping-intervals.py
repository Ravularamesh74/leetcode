class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        # Sort indices based on interval right endpoints
        order = sorted(range(n), key=lambda i: intervals[i][1])
        rights = [intervals[i][1] for i in order]
        
        # prev[p] stores (score, chosen_indices) for taking k-1 intervals among prefix p
        prev = [(0, [])] * (n + 1)
        
        # We can pick up to 4 non-overlapping intervals
        for _ in range(4):
            cur = [(0, [])] * (n + 1)
            for p in range(1, n + 1):
                i = order[p - 1]
                l, r, w = intervals[i]
                
                # Find the number of intervals ending strictly before current start time l
                j = bisect_left(rights, l)
                
                # Option 1: Include current interval
                prev_score, prev_ids = prev[j]
                take_option = (prev_score - w, sorted(prev_ids + [i]))
                
                # Option 2: Exclude current interval
                skip_option = cur[p - 1]
                
                # Pick the best option (maximum total score, tie-break by smallest indices lexicographically)
                cur[p] = min(take_option, skip_option)
                
            prev = cur
            
        return prev[n][1]