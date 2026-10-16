class Solution {
    static final int MOD = 1000000007;

    long[] treeSum;
    long[] treeCnt;
    long[] lazy;
    int n;

    // Push lazy updates down to children
    void push(int node, int l, int r) {
        if (lazy[node] != 0) {
            int mid = (l + r) / 2;
            apply(2 * node, l, mid, lazy[node]);
            apply(2 * node + 1, mid + 1, r, lazy[node]);
            lazy[node] = 0;
        }
    }

    void apply(int node, int l, int r, long val) {
        int len = (r - l + 1);
        // (x + val)^2 = x^2 + 2*val*x + val^2 * len
        treeSum[node] = (treeSum[node] + 2 * val * treeCnt[node] + val * val % MOD * len) % MOD;
        treeCnt[node] = (treeCnt[node] + val * len) % MOD;
        lazy[node] = (lazy[node] + val) % MOD;
    }

    // Range update: add val to range [ql, qr]
    void update(int node, int l, int r, int ql, int qr, long val) {
        if (ql > r || qr < l) return;
        if (ql <= l && r <= qr) {
            apply(node, l, r, val);
            return;
        }
        push(node, l, r);
        int mid = (l + r) / 2;
        update(2 * node, l, mid, ql, qr, val);
        update(2 * node + 1, mid + 1, r, ql, qr, val);
        treeSum[node] = (treeSum[2 * node] + treeSum[2 * node + 1]) % MOD;
        treeCnt[node] = (treeCnt[2 * node] + treeCnt[2 * node + 1]) % MOD;
    }

    public int sumCounts(int[] nums) {
        n = nums.length;
        treeSum = new long[4 * n];
        treeCnt = new long[4 * n];
        lazy = new long[4 * n];

        java.util.Map<Integer, Integer> lastOccurrence = new java.util.HashMap<>();
        long totalSum = 0;
        long currentSumOfSquares = 0;

        for (int j = 0; j < n; j++) {
            int last = lastOccurrence.getOrDefault(nums[j], -1);
            // Update the range [last + 1, j] by adding 1 to distinct counts
            update(1, 0, n - 1, last + 1, j, 1);
            lastOccurrence.put(nums[j], j);

            // treeSum[1] now holds the sum of squares of all subarrays ending at index j
            totalSum = (totalSum + treeSum[1]) % MOD;
        }

        return (int) totalSum;
    }
}