/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var totalWaviness = function(num1, num2) {

    function solve(n) {
        if (n <= 0) return 0;

        const digits = String(n).split('').map(Number);
        const memo = new Map();

        function dfs(pos, tight, started, len, prev2, prev1) {
            if (pos === digits.length) {
                return [1, 0]; // [count, totalWaviness]
            }

            const key =
                pos + "|" +
                (tight ? 1 : 0) + "|" +
                (started ? 1 : 0) + "|" +
                len + "|" +
                prev2 + "|" +
                prev1;

            if (!tight && memo.has(key)) {
                return memo.get(key);
            }

            const limit = tight ? digits[pos] : 9;

            let count = 0;
            let total = 0;

            for (let d = 0; d <= limit; d++) {
                const ntight = tight && d === limit;

                if (!started && d === 0) {
                    const [c, t] = dfs(
                        pos + 1,
                        ntight,
                        false,
                        0,
                        -1,
                        -1
                    );

                    count += c;
                    total += t;
                }
                else if (!started) {
                    const [c, t] = dfs(
                        pos + 1,
                        ntight,
                        true,
                        1,
                        -1,
                        d
                    );

                    count += c;
                    total += t;
                }
                else if (len === 1) {
                    const [c, t] = dfs(
                        pos + 1,
                        ntight,
                        true,
                        2,
                        prev1,
                        d
                    );

                    count += c;
                    total += t;
                }
                else {
                    let add = 0;

                    if (
                        (prev1 > prev2 && prev1 > d) ||
                        (prev1 < prev2 && prev1 < d)
                    ) {
                        add = 1;
                    }

                    const [c, t] = dfs(
                        pos + 1,
                        ntight,
                        true,
                        2,
                        prev1,
                        d
                    );

                    count += c;
                    total += t + add * c;
                }
            }

            const res = [count, total];

            if (!tight) {
                memo.set(key, res);
            }

            return res;
        }

        return dfs(0, true, false, 0, -1, -1)[1];
    }

    return solve(num2) - solve(num1 - 1);
};