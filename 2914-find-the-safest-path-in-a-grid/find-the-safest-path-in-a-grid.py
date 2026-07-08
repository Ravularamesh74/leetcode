from collections import deque
import heapq

class Solution(object):
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        
        # If start or end contains a thief, safeness factor is instantly 0
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # Step 1: Multi-source BFS to calculate minimum distance to any thief for each cell
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
        # Step 2: Max-Heap Dijkstra to find path maximizing the minimum safeness factor
        # Format: (-safeness_factor, r, c) -> Negative for max-heap behavior
        max_heap = [(-dist[0][0], 0, 0)]
        max_safeness = [[-1] * n for _ in range(n)]
        max_safeness[0][0] = dist[0][0]
        
        while max_heap:
            d, r, c = heapq.heappop(max_heap)
            d = -d  # Convert back to positive
            
            # If we reached the destination, this is our maximum safeness factor
            if r == n - 1 and c == n - 1:
                return d
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    # The safeness of moving to the next cell is limited by the current path's safeness 
                    # and the next cell's personal distance to a thief
                    next_safeness = min(d, dist[nr][nc])
                    
                    if next_safeness > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = next_safeness
                        heapq.heappush(max_heap, (-next_safeness, nr, nc))
                        
        return 0