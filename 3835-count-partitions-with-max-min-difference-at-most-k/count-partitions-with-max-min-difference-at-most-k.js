/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countPartitions = function(nums, k) {
    const MOD = 1e9 + 7;
    const n = nums.length;

    let dp = new Array(n + 1).fill(0);
    let prefix = new Array(n + 1).fill(0);

    dp[0] = 1;
    prefix[0] = 1;

    let minDeque = [];
    let maxDeque = [];
    let left = 0;

    for (let right = 0; right < n; right++) {

        // Maintain min deque
        while (minDeque.length && nums[minDeque[minDeque.length - 1]] >= nums[right]) {
            minDeque.pop();
        }
        minDeque.push(right);

        // Maintain max deque
        while (maxDeque.length && nums[maxDeque[maxDeque.length - 1]] <= nums[right]) {
            maxDeque.pop();
        }
        maxDeque.push(right);

        // Shrink window if invalid
        while (nums[maxDeque[0]] - nums[minDeque[0]] > k) {
            if (minDeque[0] === left) minDeque.shift();
            if (maxDeque[0] === left) maxDeque.shift();
            left++;
        }

        // DP transition
        dp[right + 1] = (prefix[right] - (left > 0 ? prefix[left - 1] : 0) + MOD) % MOD;

        // Update prefix sum
        prefix[right + 1] = (prefix[right] + dp[right + 1]) % MOD;
    }

    return dp[n];

};