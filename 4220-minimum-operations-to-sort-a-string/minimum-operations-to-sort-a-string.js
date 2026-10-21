/**
 * @param {string} s
 * @return {number}
 */
var minOperations = function(s) {
    const n = s.length;
    
    // Helper to check if string is sorted
    const isSorted = (str) => {
        for (let i = 0; i < str.length - 1; i++) {
            if (str[i] > str[i + 1]) return false;
        }
        return true;
    };

    // Case 0: Already sorted
    if (isSorted(s)) return 0;

    // If length is 2 and not sorted, it's impossible to pick a *proper* substring
    if (n === 2) return -1;

    // Find min and max characters
    let minChar = s[0], maxChar = s[0];
    for (let i = 1; i < n; i++) {
        if (s[i] < minChar) minChar = s[i];
        if (s[i] > maxChar) maxChar = s[i];
    }

    // Case 1: Min is at the start (proper suffix can be sorted) OR Max is at the end (proper prefix can be sorted)
    if (s[0] === minChar || s[n - 1] === maxChar) {
        return 1;
    }

    // Check conditions for 3 operations:
    // If the maximum element is uniquely at the start and the minimum element is uniquely at the end
    let minCount = 0, maxCount = 0;
    for (let char of s) {
        if (char === minChar) minCount++;
        if (char === maxChar) maxCount++;
    }

    if (s[0] === maxChar && maxCount === 1 && s[n - 1] === minChar && minCount === 1) {
        return 3;
    }

    // Fallback: 2 operations are enough for all other valid cases
    return 2;
};