/**
 * @param {number[]} source
 * @param {number[]} target
 * @param {number[][]} allowedSwaps
 * @return {number}
 */
var minimumHammingDistance = function(source, target, allowedSwaps) {

    let n = source.length;

    // Union-Find
    let parent = Array(n).fill(0).map((_, i) => i);

    function find(x) {
        if (parent[x] !== x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    function union(a, b) {
        let pa = find(a);
        let pb = find(b);
        if (pa !== pb) parent[pa] = pb;
    }

    // Build components
    for (let [a, b] of allowedSwaps) {
        union(a, b);
    }

    // Group indices
    let groups = new Map();
    for (let i = 0; i < n; i++) {
        let root = find(i);
        if (!groups.has(root)) groups.set(root, []);
        groups.get(root).push(i);
    }

    let mismatch = 0;

    // Process each group
    for (let indices of groups.values()) {
        let count = new Map();

        // Count source values
        for (let i of indices) {
            count.set(source[i], (count.get(source[i]) || 0) + 1);
        }

        // Match target
        for (let i of indices) {
            if (count.get(target[i]) > 0) {
                count.set(target[i], count.get(target[i]) - 1);
            } else {
                mismatch++;
            }
        }
    }

    return mismatch;
};