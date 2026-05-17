/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {

    let i = nums.length - 2;

    // Step 1:
    // Find first decreasing element
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }

    // Step 2:
    // Find next greater element from right
    if (i >= 0) {

        let j = nums.length - 1;

        while (nums[j] <= nums[i]) {
            j--;
        }

        // swap
        [nums[i], nums[j]] = [nums[j], nums[i]];
    }

    // Step 3:
    // Reverse remaining suffix
    reverse(nums, i + 1, nums.length - 1);
};

function reverse(arr, left, right) {

    while (left < right) {

        [arr[left], arr[right]] = [arr[right], arr[left]];

        left++;
        right--;
    }
}