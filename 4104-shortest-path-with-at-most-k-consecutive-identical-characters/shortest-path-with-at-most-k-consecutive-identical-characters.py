import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """:type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Min-heap storing (distance, node, consecutive_count)
        pq = [(0, 0, 1)]
        
        # Dictionary or memo to store minimum distance to each state (u, count)
        min_dist = {}
        min_dist[(0, 1)] = 0
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            # If we reached the destination node
            if u == n - 1:
                return d
                
            # If a shorter path to this state was already processed, skip
            if d > min_dist.get((u, count), float('inf')):
                continue
                
            for v, w in adj[u]:
                # Determine the next consecutive character count
                if labels[v] == labels[u]:
                    next_count = count + 1
                else:
                    next_count = 1
                    
                # Prune paths exceeding the limit k
                if next_count > k:
                    continue
                    
                next_dist = d + w
                state = (v, next_count)
                
                if next_dist < min_dist.get(state, float('inf')):
                    min_dist[state] = next_dist
                    heapq.heappush(pq, (next_dist, v, next_count))
                    
        # Find the minimum cost to reach node n - 1 across all valid counts
        ans = float('inf')
        for c in range(1, k + 1):
            if (n - 1, c) in min_dist:
                ans = min(ans, min_dist[(n - 1, c)])
                
        return ans if ans != float('inf') else -1