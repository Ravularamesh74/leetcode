function pathsWithMaxScore(board: string[]): number[] {
    const n = board.length;
    const MOD = 1e9 + 7;

    // Initialize DP tables
    // dpScore[i][j] stores the max score from 'S' to (i, j)
    // dpCount[i][j] stores the number of paths achieving that max score
    const dpScore: number[][] = Array.from({ length: n }, () => Array(n).fill(-1));
    const dpCount: number[][] = Array.from({ length: n }, () => Array(n).fill(0));

    // Base case at the start position 'S'
    dpScore[n - 1][n - 1] = 0;
    dpCount[n - 1][n - 1] = 1;

    // Directions we look back to: down, right, and down-right diagonal
    const dirs = [[1, 0], [0, 1], [1, 1]];

    // Iterate backwards from bottom-right to top-left
    for (let i = n - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            // Skip the starting point (already initialized) and obstacles
            if ((i === n - 1 && j === n - 1) || board[i][j] === 'X') {
                continue;
            }

            let maxPrevScore = -1;
            let pathsWithMax = 0;

            // Check all 3 incoming directions (from the perspective of moving towards 'E')
            for (const [di, dj] of dirs) {
                const ni = i + di;
                const nj = j + dj;

                // Ensure the neighbor is within bounds and reachable
                if (ni < n && nj < n && dpScore[ni][nj] !== -1) {
                    if (dpScore[ni][nj] > maxPrevScore) {
                        maxPrevScore = dpScore[ni][nj];
                        pathsWithMax = dpCount[ni][nj];
                    } else if (dpScore[ni][nj] === maxPrevScore) {
                        pathsWithMax = (pathsWithMax + dpCount[ni][nj]) % MOD;
                    }
                }
            }

            // If this cell can be reached from at least one valid path
            if (maxPrevScore !== -1) {
                const currentVal = (board[i][j] === 'E') ? 0 : parseInt(board[i][j], 10);
                dpScore[i][j] = maxPrevScore + currentVal;
                dpCount[i][j] = pathsWithMax;
            }
        }
    }

    // If 'E' at (0,0) is unreachable, return [0, 0]
    if (dpScore[0][0] === -1) {
        return [0, 0];
    }

    return [dpScore[0][0], dpCount[0][0]];
}