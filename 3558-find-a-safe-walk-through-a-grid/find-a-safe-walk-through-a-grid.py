class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        from collections import deque

        
        m, n = len(grid), len(grid[0])
        
        # Matrix to store the minimum health damage taken to reach each cell
        # Initialized to a value larger than any possible path length
        min_damage = [[float('inf')] * n for _ in range(m)]
        
        # Starting point costs whatever is at grid[0][0]
        min_damage[0][0] = grid[0][0]
        
        # Deque stores elements as (row, col)
        queue = deque([(0, 0)])
        
        # Direction vectors for up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            # If we reached the destination, we can early exit if we want,
            # but continuing ensures we find the absolute minimum.
            if r == m - 1 and c == n - 1:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    # Total damage to cross into the next cell
                    next_damage = min_damage[r][c] + grid[nr][nc]
                    
                    # If we found a path with less damage, update and queue it
                    if next_damage < min_damage[nr][nc]:
                        min_damage[nr][nc] = next_damage
                        
                        # 0-1 BFS push logic
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
        
        # Remaining health must be 1 or more
        remaining_health = health - min_damage[m-1][n-1]
        return remaining_health >= 1