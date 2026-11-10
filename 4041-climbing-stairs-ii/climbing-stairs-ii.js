/**
 * @param {number} n
 * @param {number[]} costs
 * @return {number}
 */
var climbStairs = function(n, costs) {
    // dp[j] will store the minimum cost to reach step j
    // Size is n + 1 since steps range from 0 to n
    const dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;

    for (let j = 1; j <= n; j++) {
        // We can jump to step j from i = j - 1, j - 2, or j - 3
        for (let k = 1; k <= 3; k++) {
            let i = j - k;
            if (i >= 0) {
                // costs[j - 1] because costs is 1-indexed in the description
                let jumpCost = dp[i] + costs[j - 1] + (j - i) * (j - i);
                dp[j] = Math.min(dp[j], jumpCost);
            }
        }
    }

    return dp[n];
};