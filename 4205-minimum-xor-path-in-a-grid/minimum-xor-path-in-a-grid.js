/**
 * @param {number[][]} grid
 * @return {number}
 */
var minCost = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    
    // dp[i][j] will store a Set of all possible XOR path values to reach cell (i, j)
    let dp = Array.from({ length: m }, () => Array.from({ length: n }, () => new Set()));
    
    // Base case: start cell
    dp[0][0].add(grid[0][0]);
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            // For each XOR value accumulated so far at (i, j), propagate to right and down
            for (let xorVal of dp[i][j]) {
                // Move right
                if (j + 1 < n) {
                    dp[i][j + 1].add(xorVal ^ grid[i][j + 1]);
                }
                // Move down
                if (i + 1 < m) {
                    dp[i + 1][j].add(xorVal ^ grid[i + 1][j]);
                }
            }
        }
    }
    
    // Find the minimum XOR value present in the bottom-right cell
    let minXor = Infinity;
    for (let xorVal of dp[m - 1][n - 1]) {
        minXor = Math.min(minXor, xorVal);
    }
    
    return minXor;
};