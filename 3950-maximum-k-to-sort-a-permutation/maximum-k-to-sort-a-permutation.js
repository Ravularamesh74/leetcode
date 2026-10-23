/**
 * @param {number[]} nums
 * @return {number}
 */
var sortPermutation = function(nums) {
    let maxK = -1;
    
    for (let i = 0; i < nums.length; i++) {
        // Check if the element is out of place
        if (nums[i] !== i) {
            if (maxK === -1) {
                maxK = nums[i];
            } else {
                maxK &= nums[i];
            }
        }
    }
    
    // If the array is already sorted, return 0
    return maxK === -1 ? 0 : maxK;
};