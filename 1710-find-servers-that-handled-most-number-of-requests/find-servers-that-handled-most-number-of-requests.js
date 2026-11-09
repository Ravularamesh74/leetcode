var busiestServers = function(k, arrival, load) {
    const count = new Array(k).fill(0);

    // Segment Tree: tracks available servers
    const size = 1;
    let n = 1;

    while (n < k) n *= 2;

    const tree = new Array(2 * n).fill(0);

    // Initially all servers are available
    for (let i = 0; i < k; i++) {
        tree[n + i] = 1;
    }

    for (let i = n - 1; i >= 1; i--) {
        tree[i] = tree[i * 2] + tree[i * 2 + 1];
    }

    // Update server availability
    function update(pos, value) {
        let p = n + pos;
        tree[p] = value;

        while (p > 1) {
            p = Math.floor(p / 2);
            tree[p] = tree[p * 2] + tree[p * 2 + 1];
        }
    }

    // Find first available server in range [ql, qr)
    function findFirst(node, left, right, ql, qr) {
        if (
            right <= ql ||
            left >= qr ||
            tree[node] === 0
        ) {
            return -1;
        }

        if (right - left === 1) {
            return left;
        }

        const mid = Math.floor((left + right) / 2);

        let result = findFirst(
            node * 2, left, mid, ql, qr
        );

        if (result !== -1) return result;

        return findFirst(
            node * 2 + 1, mid, right, ql, qr
        );
    }

    // Min Heap: [finishTime, serverId]
    const busy = [];

    function push(item) {
        busy.push(item);

        let i = busy.length - 1;

        while (i > 0) {
            const p = Math.floor((i - 1) / 2);

            if (busy[p][0] <= busy[i][0]) break;

            [busy[p], busy[i]] = [busy[i], busy[p]];
            i = p;
        }
    }

    function pop() {
        const result = busy[0];
        const last = busy.pop();

        if (busy.length > 0) {
            busy[0] = last;

            let i = 0;

            while (true) {
                let smallest = i;
                const l = i * 2 + 1;
                const r = i * 2 + 2;

                if (
                    l < busy.length &&
                    busy[l][0] < busy[smallest][0]
                ) {
                    smallest = l;
                }

                if (
                    r < busy.length &&
                    busy[r][0] < busy[smallest][0]
                ) {
                    smallest = r;
                }

                if (smallest === i) break;

                [busy[i], busy[smallest]] =
                    [busy[smallest], busy[i]];

                i = smallest;
            }
        }

        return result;
    }

    // Process requests
    for (let i = 0; i < arrival.length; i++) {
        const time = arrival[i];

        // Release completed servers
        while (busy.length > 0 && busy[0][0] <= time) {
            const [endTime, server] = pop();
            update(server, 1);
        }

        // Drop request if all servers are busy
        if (tree[1] === 0) continue;

        const target = i % k;

        // Find next available server
        let server = findFirst(1, 0, n, target, k);

        // Wrap around if necessary
        if (server === -1) {
            server = findFirst(1, 0, n, 0, target);
        }

        // Assign request
        update(server, 0);

        count[server]++;

        push([time + load[i], server]);
    }

    // Find busiest servers
    const maxCount = Math.max(...count);

    const result = [];

    for (let i = 0; i < k; i++) {
        if (count[i] === maxCount) {
            result.push(i);
        }
    }

    return result;
};