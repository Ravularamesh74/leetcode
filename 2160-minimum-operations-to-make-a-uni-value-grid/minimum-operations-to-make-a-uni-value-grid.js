var minOperations = function(grid, x) {
    let arr = [];

    // Step 1: Flatten
    for (let row of grid) {
        for (let val of row) {
            arr.push(val);
        }
    }

    // Step 2: Check feasibility
    let base = arr[0];
    for (let val of arr) {
        if ((val - base) % x !== 0) {
            return -1;
        }
    }

    // Step 3: Sort
    arr.sort((a, b) => a - b);

    // Step 4: Median
    let median = arr[Math.floor(arr.length / 2)];

    // Step 5: Count operations
    let ops = 0;
    for (let val of arr) {
        ops += Math.abs(val - median) / x;
    }

    return ops;
};