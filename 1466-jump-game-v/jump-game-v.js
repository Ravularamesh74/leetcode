/**
 * @param {number[]} arr
 * @param {number} d
 * @return {number}
 */
var maxJumps = function(arr, d) {
    const n = arr.length;
    const memo = new Array(n).fill(0);

    function dfs(i) {
        if (memo[i] !== 0) return memo[i];

        let best = 1;

        // Jump left
        for (let j = i - 1; j >= Math.max(0, i - d); j--) {
            if (arr[j] >= arr[i]) break;
            best = Math.max(best, 1 + dfs(j));
        }

        // Jump right
        for (let j = i + 1; j <= Math.min(n - 1, i + d); j++) {
            if (arr[j] >= arr[i]) break;
            best = Math.max(best, 1 + dfs(j));
        }

        return memo[i] = best;
    }

    let ans = 1;

    for (let i = 0; i < n; i++) {
        ans = Math.max(ans, dfs(i));
    }

    return ans;
};