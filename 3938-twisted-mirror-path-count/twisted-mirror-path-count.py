class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        
        # Helper function to find the landing spot given a starting move
        # dr, dc: initial step direction (0, 1) for right or (1, 0) for down
        def get_target(r, c, dr, dc):
            curr_r, curr_r_dir = r, dr
            curr_c, curr_c_dir = c, dc
            
            while True:
                # Check bounds
                if not (0 <= curr_r < m and 0 <= curr_c < n):
                    return None # Out of bounds
                
                # If it's an empty cell, we land here successfully
                if grid[curr_r][curr_c] == 0:
                    return (curr_r, curr_c)
                
                # If it's a mirror, we reflect:
                # If we were moving right (dc == 1), we turn down (dr = 1, dc = 0)
                # If we were moving down (dr == 1), we turn right (dr = 0, dc = 1)
                if curr_c_dir == 1:  # entered moving right
                    curr_r += 1
                    curr_r_dir, curr_c_dir = 1, 0
                else:                # entered moving down
                    curr_c += 1
                    curr_r_dir, curr_c_dir = 0, 1

        # Precompute valid transitions or use standard DP state tracking
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue
                
                # Try moving right from (i, j)
                target_right = get_target(i, j + 1, 0, 1)
                if target_right:
                    nr, nc = target_right
                    dp[nr][nc] = (dp[nr][nc] + dp[i][j]) % MOD
                
                # Try moving down from (i, j)
                target_down = get_target(i + 1, j, 1, 0)
                if target_down:
                    nr, nc = target_down
                    dp[nr][nc] = (dp[nr][nc] + dp[i][j]) % MOD
                    
        return dp[m - 1][n - 1]