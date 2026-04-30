var findValidElements = function(nums) {
    const n = nums.length;

    if (n === 1) return nums;

    let leftMax = Array(n).fill(0);
    let rightMax = Array(n).fill(0);

    // build leftMax
    leftMax[0] = -Infinity;
    for (let i = 1; i < n; i++) {
        leftMax[i] = Math.max(leftMax[i - 1], nums[i - 1]);
    }

    // build rightMax
    rightMax[n - 1] = -Infinity;
    for (let i = n - 2; i >= 0; i--) {
        rightMax[i] = Math.max(rightMax[i + 1], nums[i + 1]);
    }

    let result = [];

    for (let i = 0; i < n; i++) {
        if (i === 0 || i === n - 1 ||
            nums[i] > leftMax[i] ||
            nums[i] > rightMax[i]) {
            result.push(nums[i]);
        }
    }

    return result;
};