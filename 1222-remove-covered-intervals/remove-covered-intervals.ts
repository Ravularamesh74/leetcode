function removeCoveredIntervals(intervals: number[][]): number {
    // 1. Sort by start ascending; if starts are equal, sort by end descending
    intervals.sort((a, b) => {
        if (a[0] === b[0]) {
            return b[1] - a[1];
        }
        return a[0] - b[0];
    });

    let remainingCount = 0;
    let currentEnd = 0;

    // 2. Iterate through and check for coverage
    for (const interval of intervals) {
        // If the current interval's end extends further, it's not covered!
        if (interval[1] > currentEnd) {
            remainingCount++;
            currentEnd = interval[1]; // Update our boundary
        }
    }

    return remainingCount;
}