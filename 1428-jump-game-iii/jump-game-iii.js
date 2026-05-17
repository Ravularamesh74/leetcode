/**
 * @param {number[]} arr
 * @param {number} start
 * @return {boolean}
 */

var canReach = function(arr, start) {

    const visited = new Array(arr.length).fill(false);

    function dfs(i) {

        // out of bounds
        if (i < 0 || i >= arr.length) {
            return false;
        }

        // already visited
        if (visited[i]) {
            return false;
        }

        // found zero
        if (arr[i] === 0) {
            return true;
        }

        visited[i] = true;

        return dfs(i + arr[i]) || dfs(i - arr[i]);
    }

    return dfs(start);

};