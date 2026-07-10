class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # Create a mapping of original index to its sorted position
        # sorted_nodes will contain tuples of (value, original_index)
        sorted_nodes = sorted((nums[i], i) for i in range(n))
        
        # Position mapping from original index -> sorted index
        orig_to_sorted = [0] * n
        for sorted_idx, (_, orig_idx) in enumerate(sorted_nodes):
            orig_to_sorted[orig_idx] = sorted_idx
            
        # Precompute the greedy next step for each sorted index.
        # From sorted_idx i, we want to jump to the largest j such that:
        # sorted_nodes[j][0] - sorted_nodes[i][0] <= maxDiff
        # We can find this efficiently using two pointers.
        LOG_N = 18
        up = [[i] * LOG_N for i in range(n)]
        
        j = 0
        for i in range(n):
            while j < n and sorted_nodes[j][0] - sorted_nodes[i][0] <= maxDiff:
                j += 1
            # j - 1 is the furthest index we can jump to
            up[i][0] = j - 1
            
        # Build the binary lifting table
        for k in range(1, LOG_N):
            for i in range(n):
                up[i][k] = up[up[i][k-1]][k-1]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            # Convert original indices to their sorted array positions
            su = orig_to_sorted[u]
            sv = orig_to_sorted[v]
            
            # Ensure su is always the smaller value index to move upward/rightward
            if su > sv:
                su, sv = sv, su
                
            # Use binary lifting to see if sv is reachable from su
            # and count the minimum number of jumps required.
            steps = 0
            curr = su
            
            # Lift curr as close to sv as possible without overshooting the maximum reach
            for k in range(LOG_N - 1, -1, -1):
                if up[curr][k] < sv:
                    curr = up[curr][k]
                    steps += (1 << k)
                    
            # After the loop, up[curr][0] is the maximum single step from curr.
            # If it can cover or pass sv, then it takes 1 more step.
            if up[curr][0] >= sv:
                ans.append(steps + 1)
            else:
                ans.append(-1)
                
        return ans