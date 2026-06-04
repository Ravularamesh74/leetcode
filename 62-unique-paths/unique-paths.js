/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    let res = 1;
    const N = m + n - 2;
    const r = Math.min(m - 1, n - 1);

    for (let i = 1; i <= r; i++) {
        res = res * (N - r + i) / i;
    }

    return Math.round(res);
};