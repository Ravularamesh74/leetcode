var rotateGrid = function(grid, k) {
    let m = grid.length;
    let n = grid[0].length;
    let layers = Math.min(m, n) / 2;

    for (let layer = 0; layer < layers; layer++) {
        let elements = [];

        let top = layer, bottom = m - layer - 1;
        let left = layer, right = n - layer - 1;

        // 1. Extract elements
        // top row
        for (let j = left; j <= right; j++) {
            elements.push(grid[top][j]);
        }
        // right column
        for (let i = top + 1; i <= bottom - 1; i++) {
            elements.push(grid[i][right]);
        }
        // bottom row
        for (let j = right; j >= left; j--) {
            elements.push(grid[bottom][j]);
        }
        // left column
        for (let i = bottom - 1; i >= top + 1; i--) {
            elements.push(grid[i][left]);
        }

        // 2. Rotate
        let len = elements.length;
        let rot = k % len;

        let rotated = elements.slice(rot).concat(elements.slice(0, rot));

        // 3. Put back
        let idx = 0;

        // top row
        for (let j = left; j <= right; j++) {
            grid[top][j] = rotated[idx++];
        }
        // right column
        for (let i = top + 1; i <= bottom - 1; i++) {
            grid[i][right] = rotated[idx++];
        }
        // bottom row
        for (let j = right; j >= left; j--) {
            grid[bottom][j] = rotated[idx++];
        }
        // left column
        for (let i = bottom - 1; i >= top + 1; i--) {
            grid[i][left] = rotated[idx++];
        }
    }

    return grid;
};