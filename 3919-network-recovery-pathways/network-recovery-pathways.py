class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        import collections

        n = len(online)
        
        # Build the adjacency list
        adj = collections.defaultdict(list)
        for u, v, cost in edges:
            adj[u].append((v, cost))
            
        # Kahn's algorithm for Topological Sort
        in_degree = [0] * n
        for u, v, cost in edges:
            in_degree[v] += 1
            
        topo_order = []
        queue = collections.deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v, cost in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        # Helper function to check if a score >= 'mid' is possible
        def check(mid):
            # dp[i] stores the minimum total edge cost to reach node i from node 0
            dp = [float('inf')] * n
            dp[0] = 0
            
            for u in topo_order:
                if dp[u] == float('inf'):
                    continue
                # If we are at an intermediate node and it's offline, we can't proceed
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                    
                for v, cost in adj[u]:
                    # We can only use edges with cost >= mid
                    if cost >= mid:
                        if dp[u] + cost < dp[v]:
                            dp[v] = dp[u] + cost
                            
            return dp[n - 1] <= k

        # Binary search range for edge costs
        low = 0
        high = 10**9
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid      # 'mid' is valid, try to find a larger minimum edge-cost
                low = mid + 1
            else:
                high = mid - 1 # 'mid' is too high, reduce target
                
        return ans