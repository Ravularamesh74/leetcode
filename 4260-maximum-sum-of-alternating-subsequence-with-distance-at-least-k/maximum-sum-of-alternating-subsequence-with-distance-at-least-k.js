var maxAlternatingSum = function(nums, k) {
    const n = nums.length;

    // Coordinate compression
    let sorted = [...new Set(nums)].sort((a, b) => a - b);
    let index = new Map();
    sorted.forEach((v, i) => index.set(v, i));

    const size = sorted.length;

    // Segment Trees
    let upTree = Array(size * 4).fill(-Infinity);
    let downTree = Array(size * 4).fill(-Infinity);

    function update(tree, node, l, r, idx, val) {
        if (l === r) {
            tree[node] = Math.max(tree[node], val);
            return;
        }
        let mid = (l + r) >> 1;
        if (idx <= mid) update(tree, node * 2, l, mid, idx, val);
        else update(tree, node * 2 + 1, mid + 1, r, idx, val);

        tree[node] = Math.max(tree[node * 2], tree[node * 2 + 1]);
    }

    function query(tree, node, l, r, ql, qr) {
        if (qr < l || r < ql) return -Infinity;
        if (ql <= l && r <= qr) return tree[node];

        let mid = (l + r) >> 1;
        return Math.max(
            query(tree, node * 2, l, mid, ql, qr),
            query(tree, node * 2 + 1, mid + 1, r, ql, qr)
        );
    }

    let dpUp = Array(n).fill(0);
    let dpDown = Array(n).fill(0);

    let ans = 0;

    for (let i = 0; i < n; i++) {

        // 🔥 IMPORTANT: insert BEFORE querying
        if (i - k >= 0) {
            let j = i - k;
            let jIdx = index.get(nums[j]);

            update(upTree, 1, 0, size - 1, jIdx, dpUp[j]);
            update(downTree, 1, 0, size - 1, jIdx, dpDown[j]);
        }

        let idx = index.get(nums[i]);

        // base case
        dpUp[i] = nums[i];
        dpDown[i] = nums[i];

        // query smaller values → build UP
        if (idx > 0) {
            let bestDown = query(downTree, 1, 0, size - 1, 0, idx - 1);
            if (bestDown !== -Infinity) {
                dpUp[i] = Math.max(dpUp[i], bestDown + nums[i]);
            }
        }

        // query larger values → build DOWN
        if (idx < size - 1) {
            let bestUp = query(upTree, 1, 0, size - 1, idx + 1, size - 1);
            if (bestUp !== -Infinity) {
                dpDown[i] = Math.max(dpDown[i], bestUp + nums[i]);
            }
        }

        ans = Math.max(ans, dpUp[i], dpDown[i]);
    }

    return ans;
};