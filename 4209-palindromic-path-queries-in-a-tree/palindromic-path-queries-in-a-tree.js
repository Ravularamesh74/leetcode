var palindromePath = function(n, edges, s, queries) {
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    const LOG = Math.max(1, Math.ceil(Math.log2(n + 1)));

    const parent = Array.from(
        { length: LOG },
        () => new Int32Array(n)
    );

    const depth = new Int32Array(n);
    const tin = new Int32Array(n);
    const tout = new Int32Array(n);

    const nodeMask = new Int32Array(n);
    const rootMask = new Int32Array(n);

    for (let i = 0; i < n; i++) {
        nodeMask[i] = 1 << (s.charCodeAt(i) - 97);
    }

    // Build Euler tour, parent, depth, and root-path masks.
    let timer = 0;
    const stack = [[0, -1, 0]];

    while (stack.length > 0) {
        const top = stack[stack.length - 1];
        const u = top[0];
        const p = top[1];

        if (top[2] === 0) {
            top[2] = 1;

            parent[0][u] = p === -1 ? u : p;

            tin[u] = timer++;

            rootMask[u] =
                (p === -1 ? 0 : rootMask[p]) ^ nodeMask[u];

            for (let i = graph[u].length - 1; i >= 0; i--) {
                const v = graph[u][i];

                if (v === p) continue;

                depth[v] = depth[u] + 1;
                stack.push([v, u, 0]);
            }
        } else {
            tout[u] = timer - 1;
            stack.pop();
        }
    }

    // Binary lifting preprocessing.
    for (let k = 1; k < LOG; k++) {
        for (let u = 0; u < n; u++) {
            parent[k][u] =
                parent[k - 1][parent[k - 1][u]];
        }
    }

    // Find Lowest Common Ancestor.
    function lca(u, v) {
        if (depth[u] < depth[v]) {
            [u, v] = [v, u];
        }

        let diff = depth[u] - depth[v];

        for (let k = 0; k < LOG; k++) {
            if ((diff >> k) & 1) {
                u = parent[k][u];
            }
        }

        if (u === v) return u;

        for (let k = LOG - 1; k >= 0; k--) {
            if (parent[k][u] !== parent[k][v]) {
                u = parent[k][u];
                v = parent[k][v];
            }
        }

        return parent[0][u];
    }

    // Fenwick Tree for subtree range-XOR updates.
    const bit = new Int32Array(n + 2);

    function add(index, value) {
        for (
            let i = index + 1;
            i < bit.length;
            i += i & -i
        ) {
            bit[i] ^= value;
        }
    }

    // XOR of all updates affecting one Euler position.
    function pointQuery(index) {
        let result = 0;

        for (let i = index + 1; i > 0; i -= i & -i) {
            result ^= bit[i];
        }

        return result;
    }

    // Current root-to-node parity mask.
    function getRootMask(u) {
        return rootMask[u] ^ pointQuery(tin[u]);
    }

    const answer = [];

    for (const query of queries) {
        const parts = query.trim().split(/\s+/);

        if (parts[0] === "update") {
            const u = Number(parts[1]);
            const c = parts[2].charCodeAt(0) - 97;

            const newMask = 1 << c;
            const delta = nodeMask[u] ^ newMask;

            if (delta !== 0) {
                // Changing a node affects the root-path mask
                // of every node in its subtree.
                add(tin[u], delta);
                add(tout[u] + 1, delta);

                nodeMask[u] = newMask;
            }
        } else {
            const u = Number(parts[1]);
            const v = Number(parts[2]);

            const w = lca(u, v);

            const mask =
                getRootMask(u) ^
                getRootMask(v) ^
                nodeMask[w];

            // A palindrome permutation allows at most
            // one character to have an odd frequency.
            answer.push((mask & (mask - 1)) === 0);
        }
    }

    return answer;
};