/**
 * @param {number[][]} grid
 * @return {number}
 */
var closedIsland = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    
    // Helper function for DFS to flood-fill and sink land cells
    const dfs = function(r, c) {
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] === 1) {
            return;
        }
        // Mark as visited/water
        grid[r][c] = 1;
        
        // Explore all 4 directions
        dfs(r + 1, c);
        dfs(r - 1, c);
        dfs(r, c + 1);
        dfs(r, c - 1);
    };
    
    // 1. Flood-fill all 0s connected to the top and bottom boundaries
    for (let c = 0; c < cols; c++) {
        if (grid[0][c] === 0) dfs(0, c);
        if (grid[rows - 1][c] === 0) dfs(rows - 1, c);
    }
    
    // 2. Flood-fill all 0s connected to the left and right boundaries
    for (let r = 0; r < rows; r++) {
        if (grid[r][0] === 0) dfs(r, 0);
        if (grid[r][cols - 1] === 0) dfs(r, cols - 1);
    }
    
    // 3. Count remaining enclosed islands
    let closedIslandsCount = 0;
    for (let r = 1; r < rows - 1; r++) {
        for (let c = 1; c < cols - 1; c++) {
            if (grid[r][c] === 0) {
                closedIslandsCount++;
                dfs(r, c); // Sink this entire closed island
            }
        }
    }
    
    return closedIslandsCount;
};