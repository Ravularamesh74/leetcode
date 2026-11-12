/**
 * @param {number[]} nums
 * @return {number}
 */
var longestMonotonicSubarray = function(nums) {
    if (nums.length === 0) return 0;

    let maxLength = 1;
    let incLen = 1;
    let decLen = 1;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            incLen++;
            decLen = 1;
        } else if (nums[i] < nums[i - 1]) {
            decLen++;
            incLen = 1;
        } else {
            incLen = 1;
            decLen = 1;
        }

        maxLength = Math.max(maxLength, incLen, decLen);
    }

    return maxLength;
};