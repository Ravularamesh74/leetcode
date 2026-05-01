/**
 * @param {number[]} nums
 * @return {number}
 */
var maxRotateFunction = function(nums) {
    
    let n = nums.length;

    let sum = 0;
    let F = 0;

    // Compute sum and F(0)
    for (let i = 0; i < n; i++) {
        sum += nums[i];
        F += i * nums[i];
    }

    let max = F;

    // Compute F(k) using recurrence
    for (let k = 1; k < n; k++) {
        F = F + sum - n * nums[n - k];
        max = Math.max(max, F);
    }

    return max;
};