var twoEditWords = function(queries, dictionary) {
    const res = [];

    for (let q of queries) {
        for (let d of dictionary) {
            let diff = 0;

            for (let i = 0; i < q.length; i++) {
                if (q[i] !== d[i]) {
                    diff++;
                    if (diff > 2) break;
                }
            }

            if (diff <= 2) {
                res.push(q);
                break; // no need to check more dictionary words
            }
        }
    }

    return res;
};