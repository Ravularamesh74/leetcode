import heapq

class Solution(object):
    def maxTotalValue(self, nums, k):
        n = len(nums)

        LOG = n.bit_length()

        mx = [nums[:]]
        mn = [nums[:]]

        j = 1
        while (1 << j) <= n:
            prev_mx = mx[j - 1]
            prev_mn = mn[j - 1]
            half = 1 << (j - 1)

            cur_mx = []
            cur_mn = []

            for i in range(n - (1 << j) + 1):
                cur_mx.append(max(prev_mx[i], prev_mx[i + half]))
                cur_mn.append(min(prev_mn[i], prev_mn[i + half]))

            mx.append(cur_mx)
            mn.append(cur_mn)
            j += 1

        def value(l, r):
            length = r - l + 1
            p = length.bit_length() - 1

            maximum = max(mx[p][l], mx[p][r - (1 << p) + 1])
            minimum = min(mn[p][l], mn[p][r - (1 << p) + 1])

            return maximum - minimum

        heap = []

        for l in range(n):
            r = n - 1
            v = value(l, r)
            heapq.heappush(heap, (-v, l, r))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)
            ans += -neg_v

            if r > l:
                nr = r - 1
                nv = value(l, nr)
                heapq.heappush(heap, (-nv, l, nr))

        return ans