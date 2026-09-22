class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_counts = [[0] * k for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)

    def _merge(self, tree_idx, left_idx, right_idx):
        p_left = self.tree_prod[left_idx]
        self.tree_prod[tree_idx] = (p_left * self.tree_prod[right_idx]) % self.k
        
        # Copy left counts
        counts = list(self.tree_counts[left_idx])
        
        # Add right counts transformed by left total product
        right_counts = self.tree_counts[right_idx]
        for r in range(self.k):
            if right_counts[r]:
                new_rem = (p_left * r) % self.k
                counts[new_rem] += right_counts[r]
                
        self.tree_counts[tree_idx] = counts

    def build(self, nums, tree_idx, l, r):
        if l == r:
            val = nums[l] % self.k
            self.tree_prod[tree_idx] = val
            counts = [0] * self.k
            counts[val] = 1
            self.tree_counts[tree_idx] = counts
            return

        mid = (l + r) // 2
        self.build(nums, 2 * tree_idx + 1, l, mid)
        self.build(nums, 2 * tree_idx + 2, mid + 1, r)
        self._merge(tree_idx, 2 * tree_idx + 1, 2 * tree_idx + 2)

    def update(self, tree_idx, l, r, index, val):
        if l == r:
            rem = val % self.k
            self.tree_prod[tree_idx] = rem
            counts = [0] * self.k
            counts[rem] = 1
            self.tree_counts[tree_idx] = counts
            return

        mid = (l + r) // 2
        if index <= mid:
            self.update(2 * tree_idx + 1, l, mid, index, val)
        else:
            self.update(2 * tree_idx + 2, mid + 1, r, index, val)
        self._merge(tree_idx, 2 * tree_idx + 1, 2 * tree_idx + 2)

    def query(self, tree_idx, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree_prod[tree_idx], list(self.tree_counts[tree_idx])

        mid = (l + r) // 2
        if qr <= mid:
            return self.query(2 * tree_idx + 1, l, mid, ql, qr)
        if ql > mid:
            return self.query(2 * tree_idx + 2, mid + 1, r, ql, qr)

        left_prod, left_counts = self.query(2 * tree_idx + 1, l, mid, ql, qr)
        right_prod, right_counts = self.query(2 * tree_idx + 2, mid + 1, r, ql, qr)

        res_prod = (left_prod * right_prod) % self.k
        res_counts = list(left_counts)
        for r_rem in range(self.k):
            if right_counts[r_rem]:
                new_rem = (left_prod * r_rem) % self.k
                res_counts[new_rem] += right_counts[r_rem]

        return res_prod, res_counts


class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        st = SegmentTree(nums, k)
        ans = []

        for index, val, start, x in queries:
            # Update element
            st.update(0, 0, n - 1, index, val)
            
            # Query prefix product remainders in [start, n - 1]
            _, counts = st.query(0, 0, n - 1, start, n - 1)
            ans.append(counts[x])

        return ans