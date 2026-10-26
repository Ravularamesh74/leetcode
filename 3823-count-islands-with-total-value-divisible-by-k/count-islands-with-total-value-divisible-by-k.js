/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var countIslands = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    let count = 0;
    
    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] > 0) {
                // Start a BFS traversal for the island
                let islandSum = 0;
                let queue = [[i, j]];
                
                // Mark as visited by setting to 0
                islandSum += grid[i][j];
                grid[i][j] = 0;
                
                let head = 0;
                while (head < queue.length) {
                    const [r, c] = queue[head++];
                    
                    for (const [dr, dc] of directions) {
                        const nr = r + dr;
                        const nc = c + dc;
                        
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0) {
                            islandSum += grid[nr][nc];
                            grid[nr][nc] = 0; // Mark as visited
                            queue.push([nr, nc]);
                        }
                    }
                }
                
                // Check if the total value of the island is divisible by k
                if (islandSum % k === 0) {
                    count++;
                }
            }
        }
    }
    
    return count;
};