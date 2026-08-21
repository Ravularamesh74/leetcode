/**
 * @param {number[]} coins
 * @param {number} k
 * @return {number}
 */
var findKthSmallest = function(coins, k) {
    // Helper: gcd
    const gcd = (a, b) => b === 0 ? a : gcd(b, a % b);
    // Helper: lcm
    const lcm = (a, b) => a / gcd(a, b) * b;

    // Count how many distinct multiples ≤ x
    const count = (x) => {
        let res = 0;
        const n = coins.length;
        // Inclusion-Exclusion over subsets
        for (let mask = 1; mask < (1 << n); mask++) {
            let bits = 0, l = 1;
            for (let i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    bits++;
                    l = lcm(l, coins[i]);
                    if (l > x) break; // avoid overflow
                }
            }
            if (l <= x) {
                res += (bits % 2 === 1 ? 1 : -1) * Math.floor(x / l);
            }
        }
        return res;
    };

    // Binary search
    let left = 1, right = Math.max(...coins) * k;
    while (left < right) {
        let mid = Math.floor((left + right) / 2);
        if (count(mid) >= k) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
};
