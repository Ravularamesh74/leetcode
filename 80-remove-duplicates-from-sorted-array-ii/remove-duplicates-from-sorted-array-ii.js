/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {

    let k = 2;

    // If array size <= 2, all elements are valid
    if (nums.length <= 2) return nums.length;

    for (let i = 2; i < nums.length; i++) {

       
        if (nums[i] !== nums[k - 2]) {
            nums[k] = nums[i];
            k++;
        }
    }

    return k;

};