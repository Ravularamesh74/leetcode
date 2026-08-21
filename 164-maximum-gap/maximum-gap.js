var maximumGap = function(nums) {
    const n = nums.length;

    if (n < 2) return 0;

    let min = nums[0];
    let max = nums[0];

    // Find minimum and maximum
    for (const num of nums) {
        min = Math.min(min, num);
        max = Math.max(max, num);
    }

    if (min === max) return 0;

    // Minimum possible maximum gap
    const bucketSize = Math.max(
        1,
        Math.ceil((max - min) / (n - 1))
    );

    const bucketCount = Math.floor(
        (max - min) / bucketSize
    ) + 1;

    const bucketMin = new Array(bucketCount).fill(Infinity);
    const bucketMax = new Array(bucketCount).fill(-Infinity);

    // Put numbers into buckets
    for (const num of nums) {
        const index = Math.floor((num - min) / bucketSize);

        bucketMin[index] = Math.min(bucketMin[index], num);
        bucketMax[index] = Math.max(bucketMax[index], num);
    }

    let answer = 0;
    let previousMax = min;

    // Find maximum gap between non-empty buckets
    for (let i = 0; i < bucketCount; i++) {
        if (bucketMin[i] === Infinity) {
            continue;
        }

        answer = Math.max(
            answer,
            bucketMin[i] - previousMax
        );

        previousMax = bucketMax[i];
    }

    return answer;
};