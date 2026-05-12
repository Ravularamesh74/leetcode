/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let result = [];

    function backtrack(start, path, total) {
        // Base Case
        if (total === target) {
            result.push([...path]);
            return;
        }

        if (total > target) {
            return;
        }

        // Try every candidate starting from 'start'
        for (let i = start; i < candidates.length; i++) {
            path.push(candidates[i]);

            // same index i because we can reuse elements
            backtrack(i, path, total + candidates[i]);

            // backtrack
            path.pop();
        }
    }

    backtrack(0, [], 0);

    return result;
};