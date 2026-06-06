/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    nums.sort((a, b) => a - b);

    const result = [];
    const path = [];
    const used = new Array(nums.length).fill(false);

    function backtrack() {
        if (path.length === nums.length) {
            result.push([...path]);
            return;
        }

        for (let i = 0; i < nums.length; i++) {
            if (used[i]) continue;

            // Skip duplicates
            if (
                i > 0 &&
                nums[i] === nums[i - 1] &&
                !used[i - 1]
            ) {
                continue;
            }

            used[i] = true;
            path.push(nums[i]);

            backtrack();

            path.pop();
            used[i] = false;
        }
    }

    backtrack();
    return result;
};