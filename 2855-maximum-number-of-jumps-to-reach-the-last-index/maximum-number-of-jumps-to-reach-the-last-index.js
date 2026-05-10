
    /**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var maximumJumps = function(nums, target) {
    let n = nums.length;

    // dp[i] = max jumps to reach i
    let dp = new Array(n).fill(-1);

    dp[0] = 0;

    for (let i = 0; i < n; i++) {

        // skip unreachable positions
        if (dp[i] === -1) continue;

        for (let j = i + 1; j < n; j++) {

            let diff = nums[j] - nums[i];

            if (diff >= -target && diff <= target) {
                dp[j] = Math.max(dp[j], dp[i] + 1);
            }
        }
    }

    return dp[n - 1];

};