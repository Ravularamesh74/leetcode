/**
 * @param {number} m
 * @param {number} n
 * @return {string[]}
 */
var createGrid = function(m, n) {
    let grid = [];
    
    for (let i = 0; i < m; i++) {
        let row = "";
        for (let j = 0; j < n; j++) {
            // Keep the top row and the rightmost column free ('.'), block everything else ('#')
            if (i === 0 || j === n - 1) {
                row += ".";
            } else {
                row += "#";
            }
        }
        grid.push(row);
    }
    
    return grid;
};