/**
 * @param {character[][]} grid
 * @return {boolean}
 */
var hasValidPath = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    
    // Parity check: total path length must be even
    if ((m + n - 1) % 2 !== 0) return false;
    
    // Start must be '(' and end must be ')'
    if (grid[0][0] === ')' || grid[m - 1][n - 1] === '(') return false;
    
    const maxBalance = Math.floor((m + n) / 2);
    const memo = new Map();

    function dfs(r, c, balance) {
        // Update bracket balance
        balance += (grid[r][c] === '(' ? 1 : -1);
        
        // Invalid state
        if (balance < 0 || balance > maxBalance) return false;
        
        // Reached destination
        if (r === m - 1 && c === n - 1) return balance === 0;
        
        const key = `${r},${c},${balance}`;
        if (memo.has(key)) return memo.get(key);
        
        let result = false;
        if (r + 1 < m && dfs(r + 1, c, balance)) result = true;
        else if (c + 1 < n && dfs(r, c + 1, balance)) result = true;
        
        memo.set(key, result);
        return result;
    }

    return dfs(0, 0, 0);
};