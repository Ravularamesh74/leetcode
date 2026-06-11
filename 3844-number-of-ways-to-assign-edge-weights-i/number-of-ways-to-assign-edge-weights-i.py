from collections import deque

class Solution:
    MOD = 10**9 + 7

    def assignEdgeWeights(self, edges):
        n = len(edges) + 1

        g = [[] for _ in range(n + 1)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        q = deque([(1, 0)])
        vis = [False] * (n + 1)
        vis[1] = True

        max_depth = 0

        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)

            for nei in g[node]:
                if not vis[nei]:
                    vis[nei] = True
                    q.append((nei, depth + 1))

        return pow(2, max_depth - 1, self.MOD)