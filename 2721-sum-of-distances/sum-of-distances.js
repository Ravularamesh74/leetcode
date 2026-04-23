var distance = function(nums) {
    const map = new Map();
    const n = nums.length;
    const res = new Array(n).fill(0);

    // Step 1: group indices by value
    for (let i = 0; i < n; i++) {
        if (!map.has(nums[i])) map.set(nums[i], []);
        map.get(nums[i]).push(i);
    }

    // Step 2: process each group
    for (let positions of map.values()) {
        const k = positions.length;

        // prefix sum of indices
        const prefix = new Array(k + 1).fill(0);
        for (let i = 0; i < k; i++) {
            prefix[i + 1] = prefix[i] + positions[i];
        }

        for (let i = 0; i < k; i++) {
            const idx = positions[i];

            const left = positions[i] * i - prefix[i];
            const right = (prefix[k] - prefix[i + 1]) - positions[i] * (k - i - 1);

            res[idx] = left + right;
        }
    }

    return res;
};