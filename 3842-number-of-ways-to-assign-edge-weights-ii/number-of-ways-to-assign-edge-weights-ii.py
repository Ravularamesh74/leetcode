class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        MOD = 10 ** 9 + 7

        n = len(edges) + 1

        # Build tree
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Binary lifting setup
        LOG = (n).bit_length()
        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        # DFS to compute depths and immediate parents
        stack = [(1, 0)]
        while stack:
            node, par = stack.pop()
            parent[0][node] = par
            for nei in graph[node]:
                if nei != par:
                    depth[nei] = depth[node] + 1
                    stack.append((nei, node))

        # Build ancestor table
        for k in range(1, LOG):
            for v in range(1, n + 1):
                p = parent[k - 1][v]
                if p:
                    parent[k][v] = parent[k - 1][p]

        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = parent[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        ans = []

        for u, v in queries:
            w = lca(u, v)
            length = depth[u] + depth[v] - 2 * depth[w]

            if length == 0:
                ans.append(0)
            else:
                ans.append(pow2[length - 1])

        return ans