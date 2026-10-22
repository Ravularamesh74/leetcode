/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const n = nums.length;
    if (n === 1) return 0;

    // Check if an array is a valid rotation of a target pattern
    const getRotationShift = (arr, target) => {
        let match = -1;
        for (let i = 0; i < n; i++) {
            let ok = true;
            for (let j = 0; j < n; j++) {
                if (arr[(i + j) % n] !== target[j]) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                match = i;
                break;
            }
        }
        return match;
    };

    const increasing = Array.from({ length: n }, (_, i) => i);
    const decreasing = Array.from({ length: n }, (_, i) => n - 1 - i);

    let minOps = Infinity;

    // Strategy 1: Check if nums is a rotation of the increasing array
    let shiftInc = getRotationShift(nums, increasing);
    if (shiftInc !== -1) {
        // Option A: Just rotate left `shiftInc` times
        minOps = Math.min(minOps, shiftInc);
        // Option B: Reverse -> Rotate -> Reverse (equivalent to specific state transitions)
        // If we reverse, shift becomes (n - shiftInc) % n, then we rotate, etc.
        minOps = Math.min(minOps, 1 + (n - shiftInc) % n + 1);
    }

    // Strategy 2: Check if nums is a rotation of the decreasing array
    let shiftDec = getRotationShift(nums, decreasing);
    if (shiftDec !== -1) {
        // Option A: Reverse first (1 op), then rotate left
        minOps = Math.min(minOps, 1 + (n - shiftDec) % n);
        // Option B: Rotate left first, then reverse
        minOps = Math.min(minOps, shiftDec + 1);
    }

    return minOps === Infinity ? -1 : minOps;
};