/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {

    function findFirst() {

        let left = 0;
        let right = nums.length - 1;

        let first = -1;

        while (left <= right) {

            let mid = Math.floor((left + right) / 2);

            if (nums[mid] === target) {
                first = mid;
                right = mid - 1; // continue searching left
            }
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }

        return first;
    }

    function findLast() {

        let left = 0;
        let right = nums.length - 1;

        let last = -1;

        while (left <= right) {

            let mid = Math.floor((left + right) / 2);

            if (nums[mid] === target) {
                last = mid;
                left = mid + 1; // continue searching right
            }
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }

        return last;
    }

    return [findFirst(), findLast()];
};